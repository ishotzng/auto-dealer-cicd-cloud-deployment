
# Stage 1: Build Python dependencies
FROM python:3.14-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# Stage 2: Production image
FROM python:3.14-slim AS production

# Update Debian packages to include available security fixes
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python runtime settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install application dependencies
COPY --from=builder /wheels /wheels
COPY requirements.txt .

RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt \
    && rm -rf /wheels \
    && rm requirements.txt

# Upgrade all Python packages identified by Trivy
RUN python -m pip install --no-cache-dir --upgrade --force-reinstall \
    "jaraco.context==6.1.0" \
    "msgpack==1.2.3" \
    "setuptools==78.1.1" \
    "urllib3==2.8.0" \
    "wheel==0.46.2"

# Verify that the required secure versions are installed
RUN python -c "from importlib.metadata import version; packages = {'jaraco.context': '6.1.0', 'msgpack': '1.2.3', 'setuptools': '78.1.1', 'urllib3': '2.8.0', 'wheel': '0.46.2'}; [print(f'{name}: {version(name)}') for name in packages]; assert all(version(name) == expected for name, expected in packages.items()), 'Security package version check failed'"

# Copy application source code
COPY app/ ./app/

# Create a non-root application user
RUN useradd --create-home appuser \
    && mkdir -p /app/data \
    && chown -R appuser:appuser /app

USER appuser

# Application port
EXPOSE 8000

# Container health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)" || exit 1

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


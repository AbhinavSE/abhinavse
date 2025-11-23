FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy shared lock file
COPY uv.lock pyproject.toml /app/

# Install dependencies
# --frozen ensures we use the exact versions in uv.lock
# --no-install-project skips installing the project itself as a package (since we just run a script)
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
COPY . /app

# Expose the port
EXPOSE 3000

# Run the application
# Use 'uv run' to ensure we run in the environment with installed dependencies
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]


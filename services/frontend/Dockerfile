FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

# Copy shared dependency files from root context
COPY uv.lock pyproject.toml /app/
RUN uv sync --frozen --no-install-project --no-dev

# Copy the frontend service code
COPY services/frontend /app/services/frontend

# Expose the port
EXPOSE 3000

# Run the application
CMD ["uv", "run", "uvicorn", "services.frontend.main:app", "--host", "0.0.0.0", "--port", "3000"]


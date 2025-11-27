FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

# Copy shared dependency files
COPY uv.lock pyproject.toml /app/
RUN uv sync --frozen --no-install-project --no-dev

# Copy the simulator code
COPY services/backend /app/services/backend

# Run the simulator script
CMD ["uv", "run", "python", "services/backend/main.py"]


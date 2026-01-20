FROM python:3.12-slim

WORKDIR /app

# Установим curl для установки uv
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Установка uv (в /root/.local/bin/uv) и добавление в PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && ln -s /root/.local/bin/uv /usr/local/bin/uv

# Копируем описание проекта и lock-файл и ставим зависимости через uv
COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen --no-dev

# Копируем исходный код приложения
COPY app ./app

# Запускаем через uv, чтобы использовалось окружение, собранное uv sync
CMD ["uv", "run", "python", "-m", "app.scheduler"]


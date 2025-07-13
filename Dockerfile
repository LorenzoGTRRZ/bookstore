# Etapa base com Python
FROM python:3.12.1-slim AS python-base

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="/opt/poetry/bin:$VENV_PATH/bin:$PATH"

# Instala dependências de sistema e Poetry
RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential libpq-dev gcc \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho e copia só arquivos essenciais para instalar dependências
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Instala dependências com Poetry
RUN poetry install --no-dev
RUN poetry install

RUN pip install whitenoise

# Copia o restante do projeto
WORKDIR /app/
COPY . /app/

# Expõe a porta do Django
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
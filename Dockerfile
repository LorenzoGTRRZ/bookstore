# Estágio 1: Build das dependências
FROM python:3.12.1-slim as builder

# Define variáveis de ambiente para o Poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PATH="$POETRY_HOME/bin:$PATH" 
# Instala dependências de sistema necessárias
# Inclui git, build-essential, libpq-dev, gcc para compilação de psycopg2
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry usando pip
RUN pip install poetry

# Instala o psycopg2-binary diretamente (melhor para Docker)
RUN pip install psycopg2-binary

# Define o diretório de trabalho para as operações do Poetry
WORKDIR /opt/pysetup

# Copia apenas os arquivos de definição de dependências (para cache do Docker)
COPY poetry.lock pyproject.toml ./

# Instala as dependências do projeto (apenas produção e sem instalar o projeto raiz)
RUN poetry install --only main --no-root

# Estágio 2: Cria a imagem final, mais leve
FROM python:3.12.1-slim

# Define variáveis de ambiente para o ambiente virtual copiado
ENV VIRTUAL_ENV="/opt/pysetup/.venv" \
    PATH="/opt/pysetup/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 

# Copia o ambiente virtual do estágio de construção
COPY --from=builder /opt/pysetup/.venv /opt/pysetup/.venv

# Define o diretório de trabalho para o código da aplicação
WORKDIR /app

# Copia todo o código da sua aplicação para o contêiner
COPY . /app/

# Expõe a porta 8000, onde o Django vai escutar
EXPOSE 8000

# Comando para rodar migrações do banco de dados e iniciar o servidor Django
# Em produção, você usaria um servidor WSGI (Gunicorn/uWSGI) e migraria separadamente.
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
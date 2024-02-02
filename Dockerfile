FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++ procps \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN huggingface-cli download TheBloke/phi-2-GGUF phi-2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

COPY /app /app

CMD ["gunicorn", "--chdir", "app", "--config", "app/gunicorn_config.py", "server:app", "--timeout", "600"]

EXPOSE 8000
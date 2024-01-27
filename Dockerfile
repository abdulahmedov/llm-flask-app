FROM python:3.10-slim-buster

WORKDIR /

RUN apt-get update && apt-get install -y gcc g++ procps

COPY static /static
COPY templates /templates
COPY app.py /app.py
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN huggingface-cli download TheBloke/phi-2-GGUF phi-2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

CMD ["python", "app.py"]

EXPOSE 8000
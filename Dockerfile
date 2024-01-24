FROM python:3.10-slim-buster

WORKDIR /

RUN apt-get update && apt-get install -y gcc g++ procps

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN huggingface-cli download TheBloke/phi-2-GGUF phi-2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

COPY static /static
COPY templates /templates

RUN pip install flask

COPY app.py /app.py

CMD ["python", "capp.py"]

EXPOSE 5000
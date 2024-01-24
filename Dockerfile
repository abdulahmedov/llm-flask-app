# Use python as base image
FROM python:3.10-slim-buster

WORKDIR /

RUN apt-get update && apt-get install -y gcc g++ procps

# Install the needed packages

RUN pip install -r requirements.txt

RUN huggingface-cli download TheBloke/phi-2-GGUF phi-2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

# Run llama_7b_chat.py when the container launches
CMD ["python", "app.py"]

# Expose port 5000 outside of the container
EXPOSE 5000

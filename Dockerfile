FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 unzip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
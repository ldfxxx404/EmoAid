FROM alpine:latest

WORKDIR /app

RUN apk update && \
    apk add --no-cache \
        python3 \
        py3-pip

RUN python3 -m venv /app/venv

COPY . .

RUN /app/venv/bin/pip install --no-cache-dir -r req.txt

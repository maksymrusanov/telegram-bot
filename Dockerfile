FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y firefox-esr geckodriver libgtk-3-0 libdbus-glib-1-2 libasound2 libx11-xcb1 libxtst6 libnss3 libxrandr2 libxss1 libatk1.0-0 libatk-bridge2.0-0 libdrm2 libgbm1 libxcomposite1 libxdamage1 libxfixes3 && \
    rm -rf /var/lib/apt/lists/*
    firefox-esr geckodriver \
    libgtk-3-0 libdbus-glib-1-2 libasound2 libx11-xcb1 \
    libxtst6 libnss3 libxrandr2 libxss1 libatk1.0-0 \
    libatk-bridge2.0-0 libdrm2 libgbm1 libxcomposite1 \
    libxdamage1 libxfixes3 \
    && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

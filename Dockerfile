FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    firefox-esr \
    libgtk-3-0 libdbus-glib-1-2 libasound2 libx11-xcb1 \
    libxtst6 libnss3 libxrandr2 libxss1 libatk1.0-0 \
    libatk-bridge2.0-0 libdrm2 libgbm1 libxcomposite1 \
    libxdamage1 libxfixes3 wget unzip && \
    rm -rf /var/lib/apt/lists/*

RUN GECKO_VERSION=v0.36.0 && \
    wget -q "https://github.com/mozilla/geckodriver/releases/download/$GECKO_VERSION/geckodriver-$GECKO_VERSION-linux64.tar.gz" && \
    tar -xzf "geckodriver-$GECKO_VERSION-linux64.tar.gz" && \
    mv geckodriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm "geckodriver-$GECKO_VERSION-linux64.tar.gz"

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN python parser_folder/db/database.py

CMD ["python", "bot_main.py"]

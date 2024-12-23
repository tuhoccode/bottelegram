FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:99
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    xvfb \
    libgdk-pixbuf2.0-0 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    fonts-liberation \
    libnspr4 \
    libxtst6 \
    ca-certificates \
    xclip \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

RUN CHROME_VERSION=$(google-chrome --version | awk '{ print $3 }' | cut -d'.' -f1) \
    && echo "Chrome Version: $CHROME_VERSION"

RUN LATEST_CHROMEDRIVER=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -q "https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
    selenium \
    pyperclip \
    python-telegram-bot \
    webdriver-manager

WORKDIR /app

COPY . /app

CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 & python botid.py"]
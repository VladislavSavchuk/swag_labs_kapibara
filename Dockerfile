# Используем базовый образ Jenkins
FROM jenkins/jenkins:latest

# Выполняем команды от имени суперпользователя
USER root

# Обновляем список пакетов и устанавливаем необходимые зависимости
RUN apt-get update && \
    apt-get install -y wget curl unzip gnupg2 build-essential libssl-dev libreadline-dev zlib1g-dev \
    libnss3 libgdk-pixbuf2.0-0 libgtk-3-0 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libxtst6 \
    libxss1 libatspi2.0-0 libpangocairo-1.0-0 libpango-1.0-0 libcups2 libgbm1

# Установка Ruby и Bundler
RUN apt-get install -y ruby-full && \
    gem install bundler

# Установка Google Chrome
ARG CHROME_VERSION="116.0.5845.140-1"
RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb

# Установка ChromeDriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Установка xvfb для работы с браузером в headless режиме
RUN apt-get install -y xvfb

# Очищаем кэш apt для уменьшения размера образа
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Возвращаемся к пользователю Jenkins
USER jenkins

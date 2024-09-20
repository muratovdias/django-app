FROM python:3.12-slim

# Устанавливаем системные зависимости для компиляции пакетов, включая gettext и libpq-dev для psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libdbus-1-dev \
    python3-dev \
    build-essential \
    pkg-config \
    libglib2.0-dev \
    gettext \
    libcairo2-dev \
    libgirepository1.0-dev \
    libyaml-dev \
    libpq-dev  # Добавляем libpq-dev для работы с PostgreSQL

# Обновляем setuptools и устанавливаем wheel и cython через pip
RUN pip install --upgrade setuptools wheel cython

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

# Копируем весь код проекта
COPY . /app/

# Собираем статические файлы для продакшн
RUN python manage.py collectstatic --noinput

# Открываем порт для Gunicorn
EXPOSE 8000

# Запуск Gunicorn
CMD ["gunicorn", "datexns.wsgi:application", "--bind", "0.0.0.0:8000"]
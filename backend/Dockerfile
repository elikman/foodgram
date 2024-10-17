FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Выполнение миграций и сбор статики
RUN python manage.py collectstatic --no-input

RUN mkdir -p /backend_static/static/

# Копируем собранную статику в определенную директорию
RUN cp -r /app/collected_static/ . /backend_static/static/

# Открываем порт и запускаем Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodgram_backend.wsgi"]

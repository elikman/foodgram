#  Проект Foodgram

## О проекте

Социальная сеть «Фудграм» для любителей готовить и пробовать новые рецепты.
На сайте пользователи могут публиковать свои рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Зарегистрированным пользователям доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд. Для каждого рецепта можно получить прямую короткую ссылку, которая не меняется после редактирования рецепта.

## Стек

<img src="https://img.shields.io/badge/Python-FFFFFF?style=for-the-badge&logo=python&logoColor=3776AB"/><img src="https://img.shields.io/badge/django-FFFFFF?style=for-the-badge&logo=django&logoColor=082E08"/><img src="https://img.shields.io/badge/Django REST Framework-FFFFFF?style=for-the-badge&logo=&logoColor=361508"/><img src="https://img.shields.io/badge/PostgreSQL-FFFFFF?style=for-the-badge&logo=PostgreSQL&logoColor=4169E1"/><img src="https://img.shields.io/badge/Nginx-FFFFFF?style=for-the-badge&logo=Nginx&logoColor=009639"/><img src="https://img.shields.io/badge/GitHub Actions-FFFFFF?style=for-the-badge&logo=GitHub Actions&logoColor=2088FF"/><img src="https://img.shields.io/badge/Docker-FFFFFF?style=for-the-badge&logo=Docker&logoColor=2496ED"/><img src="https://img.shields.io/badge/Yandex Cloud-FFFFFF?style=for-the-badge&logo=Yandex Cloud&logoColor=5282FF"/>


### Как запустить проект через Docker:

1. Клонируйте репозиторий проекта
2. Установите и запустите докер
3. В корне проекта нужно создать файл .env и заполнить его (см.ниже)
4. Перейдите в папку infra и выполните команды в терминале:
```
docker compose -f docker-compose.production.yml up 
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```
### Как заполнить файл ```.env```:

Нужно создать файл .env в корне проекта и указать в нем следующие переменные:

```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DB_NAME=
DB_HOST=
DB_PORT=
DJANGO_SECRET_KEY=
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=
```

### Как запустить бэкенд локально без Docker:
1. Клонируйте репозиторий:
```git clone https://github.com/elikman/foodgram.git```
2. В корне проекта создайте файл .env и укажите в нем следующие переменные:
```
- POSTGRES_USER=
- POSTGRES_PASSWORD=
- POSTGRES_DB=
- DB_NAME=
- DB_HOST=
- DB_PORT=
- DJANGO_SECRET_KEY=
- DJANGO_DEBUG=False
- DJANGO_ALLOWED_HOSTS=
```
3. Перейдите в папку backend:
```cd backend```
4. Создайте виртуальное окружение:
```python -m venv venv```
5. Установите зависимости:
```pip install -r requirements.txt```
6. Выполните миграции:
```python manage.py migrate```
7. Импортируйте данные:
```
python manage.py import_ingredients
python manage.py import_tags
```
8. Запустите проект:
```python manage.py runserver```

##### Настроить Docker:
``` 
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```
##### Создать файл .env и указать переменные по примеру .env.example:
``` 
cd foodgram
sudo nano .env
```
##### Установить и запустить Nginx:
```
sudo apt install nginx -y
sudo systemctl start nginx
```
##### Настроить и включить firewall:
```
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```
##### Открыть файл Nginx и поменять настройкиб сохранить и закрыть:
```
sudo nano /etc/nginx/sites-enabled/default
```
```
server {
    listen 80;
    server_name your_domain_name.com;
    
    location / {
        proxy_set_header HOST $host;
        proxy_pass http://127.0.0.1:8000;

    }
}
```
##### Проверить корректность настроек и перезапустить Nginx: 
```
sudo nginx -t
sudo systemctl start nginx
```
##### Загрузить образы из DockerHub:
```
sudo docker compose -f docker-compose.production.yml pull
```
##### Остановить и удалить все контейнеры:
```
sudo docker compose -f docker-compose.production.yml down
```
##### Запустить контейнеры из образов в фоновом режиме: 
```
sudo docker compose -f docker-compose.production.yml up -d
```
##### Выполнить миграции: 
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate 
```
##### Собрать статику:
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
```
##### Создать суперпользователя (указать логин, e-mail, пароль):
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser 
```
##### Загрузить список ингредиентов в базу данных:
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_ingredients
``` 
##### Загрузить тестовые данные:
``` 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_tags
``` 

### Автор
Финальное задание курса [Python Backend Developer Яндекс Практикум](https://practicum.yandex.ru/backend-developer-ab/)

Выполнил  [Набиев Эльтадж](https://github.com/elikman/foodgram.git) https://t.me/bombalaev57

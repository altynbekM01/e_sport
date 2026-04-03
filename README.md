
##  Запуск проекта

### 1. В корне проекта создать `.env` по образу `.env.example` , вставить свои апи ключ от Pandascore и SECRET_KEY


### 2. Можно запустить через докер контейнер, выполнив команду

```
docker-compose up --build
```

Перейти на http://localhost:8000, и нажать кнопку Сгенерировать страницы:


---


### Также можно запустить через виртуальное окружение, предварительно создав его.

```env
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```
### Установить зависимости:

```
pip install -r requirements.txt
```
### Запустить локальный сервер Django:
```
python manage.py runserver
```


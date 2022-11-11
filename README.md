# test_login
Test DRF project for JWT authorization

# Как собрать
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate --noinput
docker-compose up

# Как работает
Эндпоинты и описание:
login/ - берет username, password и позвращает JWT токены. Так же добавлена авторизация по адресу email  
register/ - берет username, email, password1, password2, сериализует и отвечает JWT токенами
login/refresh/ - позволяет получить refresh токен
auth/ - простой view с доступом только для авторизованных

# Заметки
В качестве базы данных используется postgres, выведен наружу порт 5433, параметры подключения есть либо в Докерфайле, либо в .env
Uvicorn выступает как asgi сервер, располагается на 0.0.0.0:7777, порт 7777 выведен наружу.
Обновление токенов предполагается с помощью клиентской стороны.
Для авторизации необходимо в заголовок добавить Authorization: Bearer $(access_token).
Рефреш токены добавляются в черный список после использования.

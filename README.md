# test_login
Test DRF project for JWT authorization

# Как собрать
docker-compose build<br/>
docker-compose up -d<br/>
docker-compose exec web python manage.py migrate --noinput<br/>
docker-compose up<br/>

# Как работает
Эндпоинты и описание:<br/>
login/ - берет username, password и позвращает JWT токены. Так же добавлена авторизация по адресу email  <br/>
register/ - берет username, email, password1, password2, сериализует и отвечает JWT токенами<br/>
login/refresh/ - позволяет получить refresh токен<br/>
auth/ - простой view с доступом только для авторизованных<br/>

# Заметки
В качестве базы данных используется postgres, выведен наружу порт 5433, параметры подключения есть либо в Докерфайле, либо в .env<br/>
Uvicorn выступает как asgi сервер, располагается на 0.0.0.0:7777, порт 7777 выведен наружу.<br/>
Обновление токенов предполагается с помощью клиентской стороны.<br/>
Для авторизации необходимо в заголовок добавить Authorization: Bearer $(access_token).<br/>
Рефреш токены добавляются в черный список после использования.

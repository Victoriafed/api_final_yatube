# api_final_yatube
Проект yatube позволет пользоватлям зарегистрироваться в yatube и вести личный блог через посты. Также предоставлена возмжность подписки на интересных пользователю авторов.
____
### Как запустить проект:
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
____
### Примеры запросов:
***Получение постов***
- GET: 
http://127.0.0.1:8000/api/v1/posts/{id}/
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
***Создание поста***
- Post: 
http://127.0.0.1:8000/api/v1/posts/
```
{
"text": "string",
"image": "string",
"group": 0
}
```
***Получение комментариев***
- Get:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
[
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
]
```
____
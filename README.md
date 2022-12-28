# api_final_yatube
Проект yatube позволет пользоватлям зарегистрироваться в yatube и вести личный блог через посты. Также предоставлена возмжность подписки на интересных пользователю авторов.

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
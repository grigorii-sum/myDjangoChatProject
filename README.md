# myDjangoChatProject
Проект "myDjangoChatProject" с регистрации, авторизации и выхода из системы, а также общения в чате

---

# ЗАПУСК ПРОЕКТА
Запустить данный проект можно двумя способами: либо через "Dockerfile", либо через "manage.py"

---

## ЗАПУСК ПРОЕКТА ЧЕРЕЗ "Dockerfile"

Запустите Docker на Вашем компьютере и введите последовательно все нижеперечисленные команды:

`python3 manage.py migrate`

`pip install -r requirements.txt`

`docker build -t my-django-chat-project -f Dockerfile .`

`gunicorn myDjangoChatProject.wsgi:application —bind localhost:8000`

Проект запущен.

---

## ЗАПУСК ПРОЕКТА ЧЕРЕЗ "manage.py"

Введите последовательно все нижеперечисленные команды:

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver`

Проект запущен.

---

## СОЗДАНИЕ СУПЕРЮЗЕРА ДЛЯ ДОСТУПА К АДМИНИСТРАТИВНОЙ ПАНЕЛИ DJANGO

После ввода нижепредставленной команды нужно вести логин и пароль дважды (почту вводить необязательно):

`python3 manage.py createsuperuser`

Админка доступна по url: http://127.0.0.1:8000/admin/
# TODO app
Использовано Django(DRF), Redis, Celery

## Install
> python3 -m venv venv

> venv\Scripts\activate

> pip install -r requirements.txt

> python manage.py migrate

## Usage

> python manage.py runserver

> celery -A todo_api.celery worker —pool=solo -l info

> **Note:** Для отправки электронной почты email и пароль Gmail аккаунта отправителя берется с переменных окружения:
EMAIL_HOST_USER = os.environ['DJANGO_EMAIL']
EMAIL_HOST_PASSWORD = os.environ['DJANGO_EMAIL_PASS']

## API ENDPOINTS
### Авторизация
- POST /api/accounts/register/ - регистрация пользователя
- POST /api/accounts/login/ - авторизация
- POST /api/accounts/logout/ - выход
- POST /api/accounts/token/refresh/ - для обновления access токена
> Для работы с jwt была использована библиотека _rest_framework_simplejwt_

### Tasks(TODOs)
- GET /api/todo/ - Просмотр всех задач
- POST /api/todo/ - Создание задачи
- GET api/todo/{todo_id}/ - Просмотр задачи по id
- PATCH api/todo/{todo_id}/ - Изменение задачи по id
- DELETE api/todo/{todo_id}/ - Удаление задачи по id
> **Note:** Вы не можете удалять или изменять задачи, которые создали другие юзеры.

> При изменений статуса задачи, Вам так же приходит сообщение на почту
- api/todo/{todo_id}/execute/ - Пометить задачу выполненной и отправить сообщение создателю задачи

# TODO app
Использовал Python, Django + DRF

## Install
> python3 -m venv venv

> venv\Scripts\activate

> pip install -r requirements.txt

> python manage.py migrate

## Usage

> python manage.py runserver

> celery -A todo_api.celery worker —pool=solo -l info

### **NOTE:** вы должны сами создать DJANGO_EMAIL, DJANGO_EMAIL_PASS в своём виртуальном переменном окружений(activate.bat)
> set DJANGO_EMAIL={email} 
> 
> set DJANGO_EMAIL_PASS={email_password}
#### deactivate.bat
> set DJANGO_EMAIL=
> 
> set DJANGO_EMAIL_PASS=

## API ENDPOINTS
### _Авторизация, реализованная с помощью библиотеки_ rest_framework_simplejwt
- /api/accounts/register/ - регистрация пользователя
- /api/accounts/login/ - авторизация
- /api/accounts/logout/ - выход
- /api/accounts/token/refresh/ - для обновления access токена

### Tasks(TODOs)
- api/todo/ - Создание задачи и просмотр всех задачь
- api/todo/{todo_id}/ - Возвращение, изменение и удаление задачи
> **Note:** Вы не можете удалять или изменять задачи, которые создали другие юзеры.

> При изменений статуса задачи, Вам так же приходит сообщение на почту
- api/todo/{todo_id}/execute/ - Пометить задачу выполненной и отправка сообщения создателю задачи

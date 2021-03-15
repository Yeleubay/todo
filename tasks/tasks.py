from django.core.mail import send_mail

from todo_api.celery import app
from .models import Task


@app.task(bind=True)
def send_is_done_email(self, task_id):
    task = Task.objects.get(pk=task_id)
    if task.is_done:
        message = 'Задача: ' + task.title + '. \nОтмечено выполненной'
    else:
        message = 'Задача: ' + task.title + '. \nОтмечено не выполненной'
    send_mail(
        'Выполнение задачи',
        message,
        'yeleubayiliyas@example.com',
        [task.created_by.email],
        fail_silently=False,
    )

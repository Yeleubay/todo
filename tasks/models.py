from django.db import models
from users.models import CustomUser


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_done = models.BooleanField()
    created_by = models.ForeignKey(CustomUser, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

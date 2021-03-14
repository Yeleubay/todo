from rest_framework import serializers
from .models import Task
from users.serializers import RegistrationSerializer


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'deadline', 'is_done']


class TaskSerializer(serializers.ModelSerializer):
    created_by = RegistrationSerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


from rest_framework import serializers
from .models import Task
from users.serializers import CustomUserSerializer
from users.models import CustomUser


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'deadline', 'is_done']


class TaskSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_done'] = False
        task = Task.objects.create(**validated_data, created_by=self.context['request'].user)
        return task


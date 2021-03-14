from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail


from .serializers import TasksSerializer, TaskSerializer
from .models import Task


@api_view(["GET"])
@permission_classes([AllowAny])
def get_tasks_list(request):
    tasks = Task.objects.all()
    serializer = TasksSerializer(tasks, context={'request': request}, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_task(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, context={'request': request}, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def execute(request, pk):
    task = Task.objects.get(pk=pk)
    if not task.is_done:
        send_mail(
            'Выполнение задачи',
            'Задача "" ',
            'yeleubayiliyas@example.com',
            [task.created_by.email],
            fail_silently=False,
        )
        task.is_done = True
        task.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

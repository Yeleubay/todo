from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


from .serializers import TasksSerializer, TaskSerializer
from .models import Task
from .tasks import send_is_done_email


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
def create_task(request):
    serializer = TaskSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.user == task.created_by:
        if task.is_done != request.data['is_done']:
            send_is_done_email.delay(pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("You do not have permission for manipulations on this task",
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        if request.user == task.created_by:
            task.delete()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response("You do not have permission for manipulations on this task",
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def execute(request, pk):
    task = Task.objects.get(pk=pk)
    if not task.is_done:
        task.is_done = True
        task.save()
        send_is_done_email.delay(pk)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

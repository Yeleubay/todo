from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    user_data = request.data.get('user')
    serializer = RegistrationSerializer(data=user_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    # generating token for user created
    user = CustomUser.objects.get(email=serializer.data['email'])
    refresh = RefreshToken.for_user(user)
    return Response(
        {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)

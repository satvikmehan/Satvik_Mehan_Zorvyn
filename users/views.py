from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .serializers import SignupSerializer


@api_view(['GET'])
@permission_classes([AllowAny]) 
def hello(request):
    return Response({"message": "Hello from DRF"})


@api_view(['POST'])
@permission_classes([AllowAny]) 
def signup(request):
    try:
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({
            "message": "User created successfully",
            "user": {
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }, status=status.HTTP_201_CREATED)

    except ValidationError as e:
        return Response({
            "error": "Signup failed",
            "details": e.detail
        }, status=status.HTTP_400_BAD_REQUEST)
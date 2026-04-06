from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer

@api_view(['GET'])
@permission_classes([AllowAny]) 
def hello(request):
    return Response({"message": "Hello from DRF"})

@api_view(['POST'])
@permission_classes([AllowAny]) 
def signup(request):
    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response({
            "message": "User created successfully",
            "user": {
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }, status=status.HTTP_201_CREATED)

    return Response({
        "error": "Signup failed",
        "details": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
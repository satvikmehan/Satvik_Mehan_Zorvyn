from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SignupSerializer

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from DRF"})

@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully","user": serializer.data},status=status.HTTP_201_CREATED)
    
    return Response({"errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
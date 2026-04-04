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
        return Response({"message": "User created successfully"}, status=201)
    
    return Response(serializer.errors, status=400)
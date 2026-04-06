from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from users.permissions import RecordPermission
from .models import Record
from .serializers import RecordSerializer
from .services import get_filtered_records


@api_view(['GET', 'POST'])
@permission_classes([RecordPermission])
def records_list(request):

    # GET
    if request.method == 'GET':
        records = get_filtered_records(request.user, request)

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(records, request)

        serializer = RecordSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    # POST
    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([RecordPermission])
def record_detail(request, pk):

    try:
        record = Record.objects.get(pk=pk, user=request.user)
    except Record.DoesNotExist:
        return Response({"detail": "Record not found"}, status=404)

    # GET
    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    # PUT
    if request.method == 'PUT':
        serializer = RecordSerializer(record, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # DELETE
    if request.method == 'DELETE':
        record.delete()
        return Response(status=204)
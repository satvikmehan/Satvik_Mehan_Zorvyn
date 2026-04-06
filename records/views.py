from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from users.permissions import RecordPermission
from .models import Record
from .serializers import RecordSerializer
from .services import get_filtered_records


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, RecordPermission])
def records_list(request):

    # GET
    if request.method == 'GET':
        try:
            records = get_filtered_records(request.user, request)

            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(records, request)

            serializer = RecordSerializer(page, many=True)

            return paginator.get_paginated_response({
                "message": "Records fetched successfully",
                "data": serializer.data
            })

        except Exception as e:
            return Response({
                "error": "Failed to fetch records",
                "details": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    # POST
    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data, context={'request': request})

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)

            return Response({
                "message": "Record created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "error": "Failed to create record",
                "details": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, RecordPermission])
def record_detail(request, pk):

    try:
        record = Record.objects.get(pk=pk, user=request.user)
    except Record.DoesNotExist:
        return Response({
            "error": "Record not found"
        }, status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return Response({
            "message": "Record fetched successfully",
            "data": serializer.data
        })

    # PUT
    if request.method == 'PUT':
        serializer = RecordSerializer(
            record,
            data=request.data,
            partial=True,
            context={'request': request}
        )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message": "Record updated successfully",
                "data": serializer.data
            })

        except Exception as e:
            return Response({
                "error": "Update failed",
                "details": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    if request.method == 'DELETE':
        record.delete()
        return Response({
            "message": "Record deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
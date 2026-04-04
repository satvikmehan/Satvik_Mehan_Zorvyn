from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Record
from .serializers import RecordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def records_list(request):

    user = request.user

    #Viewer
    if request.method == 'GET':
        records = Record.objects.filter(user=user)

        #Filters
        category = request.GET.get('category')
        type_ = request.GET.get('type')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        search = request.GET.get('search')

        if category:
            records = records.filter(category=category)

        if type_:
            records = records.filter(type=type_)

        if start_date and end_date:
            records = records.filter(date__range=[start_date, end_date])

        if search:
            records = records.filter(category__icontains=search)

        #Paginator
        paginator = PageNumberPagination()
        paginator.page_size = 5

        page = paginator.paginate_queryset(records, request)
        serializer = RecordSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)


    #Admin
    elif request.method == 'POST':
        if user.role != 'admin':
            return Response({"error": "Permission denied"}, status=403)

        data = request.data.copy()
        data['user'] = user.id

        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def record_detail(request, pk):

    user = request.user

    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


    #User
    if record.user != user:
        return Response({"error": "Unauthorized"}, status=403)

    #Admin
    if user.role != 'admin':
        return Response({"error": "Permission denied"}, status=403)

    if request.method == 'PUT':
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        record.delete()
        return Response({"message": "Deleted"})
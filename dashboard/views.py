from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from records.models import Record
from collections import defaultdict

#Main
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def summary(request):
    user = request.user

    income = Record.objects.filter(user=user, type='income').aggregate(total=Sum('amount'))['total'] or 0
    expense = Record.objects.filter(user=user, type='expense').aggregate(total=Sum('amount'))['total'] or 0

    return Response({
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    })

#Category-wise API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_summary(request):
    user = request.user
    records = Record.objects.filter(user=user)

    data = {}

    for r in records:
        if r.category not in data:
            data[r.category] = 0
        data[r.category] += r.amount

    return Response(data)

#Monthly Trends API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def monthly_trends(request):
    user = request.user
    records = Record.objects.filter(user=user)

    trends = defaultdict(int)

    for r in records:
        month = r.date.strftime("%Y-%m")
        trends[month] += r.amount

    return Response(trends)
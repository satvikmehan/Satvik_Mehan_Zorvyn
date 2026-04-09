from django.db.models import Sum
from django.db.models.functions import TruncMonth
from records.models import Record


def get_summary(user, request):
    records = get_filtered_records(user, request)

    income = records.filter(type='income') \
        .aggregate(total=Sum('amount'))['total'] or 0

    expense = records.filter(type='expense') \
        .aggregate(total=Sum('amount'))['total'] or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }


def get_category_summary(user, request):
    records = get_filtered_records(user, request)

    data = (
        records
        .values('category')
        .annotate(total=Sum('amount'))
    )

    return {item['category']: item['total'] for item in data}


def get_monthly_trends(user, request):
    records = get_filtered_records(user, request)

    data = (
        records
        .annotate(month=TruncMonth('date'))
        .values('month', 'type')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    result = {}

    for item in data:
        month = item['month'].strftime("%Y-%m")

        if month not in result:
            result[month] = {"income": 0, "expense": 0}

        result[month][item['type']] = item['total']

    return result

def get_filtered_records(user, request):
    queryset = Record.objects.filter(user=user)

    start = request.GET.get('start')
    end = request.GET.get('end')
    category = request.GET.get('category')
    type_ = request.GET.get('type')

    if start and end:
        queryset = queryset.filter(date__range=[start, end])

    if category:
        queryset = queryset.filter(category=category)

    if type_:
        queryset = queryset.filter(type=type_)

    return queryset


def get_recent_activity(user, request):
    records = get_filtered_records(user, request)

    data = (
        records
        .order_by('-date')[:5]
        .values('id', 'amount', 'type', 'category', 'date')
    )

    return list(data).order_by('-date', '-id')
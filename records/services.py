from .models import Record

def get_filtered_records(user, request):
    queryset = Record.objects.filter(user=user).select_related('user')

    category = request.GET.get('category')
    type_ = request.GET.get('type')
    start = request.GET.get('start')
    end = request.GET.get('end')
    search = request.GET.get('search')

    if category:
        queryset = queryset.filter(category=category)

    if type_:
        queryset = queryset.filter(type=type_)

    if start and end:
        queryset = queryset.filter(date__range=[start, end])

    if search:
        queryset = queryset.filter(notes__icontains=search)

    return queryset
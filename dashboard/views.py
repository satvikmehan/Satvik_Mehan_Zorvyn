from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.permissions import IsViewer
from .services import get_summary, get_category_summary, get_monthly_trends


@api_view(['GET'])
@permission_classes([IsViewer])
def summary(request):
    return Response(get_summary(request.user,request))


@api_view(['GET'])
@permission_classes([IsViewer])
def category_summary(request):
    return Response(get_category_summary(request.user,request))


@api_view(['GET'])
@permission_classes([IsViewer])
def monthly_trends(request):
    return Response(get_monthly_trends(request.user,request))
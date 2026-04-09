from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsViewer
from .services import get_summary, get_category_summary, get_monthly_trends, get_recent_activity


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsViewer])
def summary(request):
    try:
        data = get_summary(request.user, request)

        return Response({
            "message": "Summary fetched successfully",
            "data": data
        })

    except Exception as e:   # acceptable for aggregation logic
        return Response({
            "error": "Failed to fetch summary",
            "details": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsViewer])
def category_summary(request):
    try:
        data = get_category_summary(request.user, request)

        return Response({
            "message": "Category summary fetched successfully",
            "data": data
        })

    except Exception as e:
        return Response({
            "error": "Failed to fetch category summary",
            "details": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsViewer])
def monthly_trends(request):
    try:
        data = get_monthly_trends(request.user, request)

        return Response({
            "message": "Monthly trends fetched successfully",
            "data": data
        })

    except Exception as e:
        return Response({
            "error": "Failed to fetch monthly trends",
            "details": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsViewer])
def recent_activity(request):
    try:
        data = get_recent_activity(request.user, request)

        return Response({
            "message": "Recent activity fetched successfully",
            "data": data
        })

    except Exception as e:
        return Response({
            "error": "Failed to fetch recent activity",
            "details": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenRefreshView
from users.jwt import CustomTokenView

def api_root(request):
    return JsonResponse({
        "message": "Finance Dashboard API",
        "endpoints": {
            "signup": "/signup/",
            "login": "/api/token/",
            "refresh_token": "/api/token/refresh/",
            "records": "/records/",
            "dashboard_summary": "/dashboard/summary/",
            "dashboard_category": "/dashboard/category/",
            "dashboard_trends": "/dashboard/trends/",
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', api_root),

    path('api/token/', CustomTokenView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('', include('users.urls')),
    path('records/', include('records.urls')),
    path('dashboard/', include('dashboard.urls')),
]
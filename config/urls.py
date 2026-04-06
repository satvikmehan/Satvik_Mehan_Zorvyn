from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Finance Dashboard API",
        "endpoints": {
            "signup": "/signup/",
            "login": "/login/",
            "records": "/records/",
            "dashboard_summary": "/dashboard/summary/",
            "dashboard_category": "/dashboard/category/",
            "dashboard_trends": "/dashboard/trends/",
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', api_root),

    path('', include('users.urls')),
    path('records/', include('records.urls')),
    path('dashboard/', include('dashboard.urls')),
]
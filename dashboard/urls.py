from django.urls import path
from .views import summary, category_summary, monthly_trends, recent_activity

urlpatterns = [
    path('summary/', summary),
    path('category/', category_summary),
    path('trends/', monthly_trends),
    path('recent/', recent_activity),
]
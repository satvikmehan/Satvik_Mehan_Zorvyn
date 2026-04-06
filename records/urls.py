from django.urls import path
from .views import records_list, record_detail

urlpatterns = [
    path('', records_list),
    path('<int:pk>/', record_detail),
]
from django.contrib import admin
from django.urls import path
from users.views import hello
from users.views import signup
from rest_framework_simplejwt.views import TokenObtainPairView
from records.views import records_list, record_detail
from dashboard.views import summary, category_summary, monthly_trends

urlpatterns = [
    #test
    path('hello/', hello),
    path('', hello),

    #Auth
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('login/', TokenObtainPairView.as_view()),

    #Record
    path('records/', records_list),
    path('records/<int:pk>/', record_detail),

    #Dashboard
    path('dashboard/summary/', summary),
    path('dashboard/category/', category_summary),
    path('dashboard/trends/', monthly_trends),
]
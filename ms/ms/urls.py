from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/', views.student_api),
    path('studentinfo/<int:pk>', views.student_api),
]

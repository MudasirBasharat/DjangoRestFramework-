from django.contrib import admin
from django.urls import path
from classapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/',views.studentapi.as_view()),
    path('studentinfo/<int:pk>',views.studentapi.as_view()),
]

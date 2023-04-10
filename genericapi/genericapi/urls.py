from django.contrib import admin
from django.urls import path
from gs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentinfo/',views.studentlist.as_view()),
    # path('studentinfo/<int:pk>',views.studentlist.as_view()),
    # path('studentinfo/',views.studentcreate.as_view()),
    # path('studentinfo/<int:pk>',views.studentcreate.as_view()),
    path('studentinfo/',views.studentretrive.as_view()),
    path('studentinfo/<int:pk>',views.studentretrive.as_view()),
]
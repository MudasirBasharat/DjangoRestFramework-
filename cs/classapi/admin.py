from django.contrib import admin
from django.contrib import admin
from .models import studentmodel

@admin.register(studentmodel)
class studentadmin(admin.ModelAdmin):
    list_display=['id','name','rollnbr','city'] 
# Register your models here.

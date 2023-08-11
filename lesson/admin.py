from django.contrib import admin
from .models import CRUD
# Register your models here.
@admin.register(CRUD)
class CRUDadmin(admin.ModelAdmin):
    list_display=['user','text','created_at','updated_at']

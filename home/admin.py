from django.contrib import admin
from .models import Treners, News
# Register your models here.

@admin.register(Treners)
class TrenersAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'updated_at']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    
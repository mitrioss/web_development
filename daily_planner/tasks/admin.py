from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Task

# Регистрируем модель Task в админке
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'description')  # Какие поля отображаются в списке
    list_filter = ('status',)  # Фильтр по статусу в админке
    search_fields = ('title', 'description')  # Поиск по названию и описанию задачи

admin.site.register(Task, TaskAdmin)

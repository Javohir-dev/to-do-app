from django.contrib import admin
from .models import Tasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "complate"]
    search_fields = ["title"]

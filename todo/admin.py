from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('task', 'created_at')  # Customize columns shown in the admin list view

admin.site.register(ToDo, ToDoAdmin)

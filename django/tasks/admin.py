from django.contrib import admin
from .models import Project, Cliente, Motocicleta, Task
from .models import Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")


@admin.register(Cliente)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created_at")
    search_fields = ("nombre",)  


@admin.register(Motocicleta)
class MotocicletaAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "cilindrada", "precio", "created_at")
    search_fields = ("marca", "modelo")
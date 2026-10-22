from django.contrib import admin
from .models import Project, Cliente


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Cliente)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created_at")
    search_fields = ("nombre",)  
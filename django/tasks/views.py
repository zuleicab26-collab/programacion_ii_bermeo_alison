from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm, ProjectForm
from .models import Project


def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, TaskFlow")


def register(request):
    """Registro de usuarios."""
    return HttpResponse("Registro de usuarios en línea")


def about_me(request):
    """Vista sobre mí."""
    return HttpResponse("Acerca de mí - Creado por Alison Bermeo")


def greeting(request, nombre):
    """Saludo con nombre."""
    return HttpResponse(f"Hola {nombre}, bienvenido a TaskFlow")


def destination(request, titulo, nombre, cargo):
    """Saludo con datos de destino."""
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es: {cargo}")


def base_triangulo(request, base, altura):
    """Cálculo del área del triángulo."""
    area = (base * altura) / 2
    return HttpResponse(f"El área del triángulo es: {area}")


def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)


def leads_like(request):
    contexto = {
        "titulo": "Programador",
        "nombre": "Alison",
        "apellido": "Bermeo",
    }
    return render(request, "leads/leads-like.html", contexto)


def lista(request):
    """Lista todos los proyectos."""
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "tasks/home.html", contexto)


def task_create(request):
    """Crea una nueva tarea."""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:project-list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})


def project_create(request):
    """Crea un nuevo proyecto."""
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:project-list")
    else:
        form = ProjectForm()

    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})
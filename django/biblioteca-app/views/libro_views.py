from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.models import Categoria, Libro
from catalogo.forms.libro_form import LibroForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def libro_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria_id', '').strip()
    libros = Libro.objects.select_related('categoria').all()
    categorias = Categoria.objects.all()
    if pista:
        libros = libros.filter(
            Q(titulo__icontains=pista) |
            Q(autor__nombre__icontains=pista) |
            Q(autor__apellido__icontains=pista) |
            Q(categoria__nombre__icontains=pista)
        )
    if categoria_id.isdigit():
        libros = libros.filter(categoria_id=int(categoria_id))

    context = {
        'libros': libros,
        'categoria_id': categoria_id,
        'pista': pista,
        'categorias': categorias,
    }
    return render(request, 'catalogo/libros/libro_list.html', context)

@login_required
@permission_required('catalogo.add_libro', raise_exception=True)
def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado correctamente.')
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'catalogo/libros/formulario.html', {'formulario': form})

@login_required
@permission_required('catalogo.change_libro', raise_exception=True)
def update_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado correctamente.')
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'catalogo/libros/formulario.html', {'formulario': form})

@login_required
@permission_required('catalogo.delete_libro', raise_exception=True)
def delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado correctamente.')
        return redirect('libro_list')
    return render(request, 'catalogo/libros/confirm_delete.html', {'libro': libro})
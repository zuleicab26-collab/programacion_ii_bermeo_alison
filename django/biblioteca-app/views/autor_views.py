from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.forms.autor_forms import AutorForm
from catalogo.models import Autor


@login_required
@permission_required('catalogo.view_autor', raise_exception=True)
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autor/autor_list.html', {'autores': autores})


@login_required
@permission_required('catalogo.add_autor', raise_exception=True)
def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado correctamente.')
            return redirect('autor_list')
    else:
        form = AutorForm()

    return render(request, 'catalogo/autor/formulario.html', {'formulario': form})


@login_required
@permission_required('catalogo.change_autor', raise_exception=True)
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado correctamente.')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)

    return render(request, 'catalogo/autor/formulario.html', {'formulario': form})


@login_required
@permission_required('catalogo.delete_autor', raise_exception=True)
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        try:
            autor.delete()
        except ProtectedError:
            messages.error(request, 'No se puede eliminar el autor porque tiene libros asociados.')
        else:
            messages.success(request, 'Autor eliminado correctamente.')
        return redirect('autor_list')

    return render(
        request,
        'catalogo/autor/autor_confirm_delete.html',
        {'autor': autor},
    )
from django.contrib import messages
from django.shortcuts import redirect, render

from catalogo.forms.categoria_form import CategoriaForm
from catalogo.models import Categoria


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'catalogo/categoria/categoria_list.html',
        {'categorias': categorias},
    )


def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()

    return render(
        request,
        'catalogo/categoria/formulario.html',
        {'formulario': form},
    )


#Mami ia me ayudo sepa que hizo o por que hizo 
def categoria_update(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(
        request,
        'catalogo/categoria/formulario.html',
        {'formulario': form},
    )


def categoria_delete(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
        return redirect('categoria_list')
    return render(
        request,
        'catalogo/categoria/categoria_confirm_delete.html',
        {'categoria': categoria},
    )
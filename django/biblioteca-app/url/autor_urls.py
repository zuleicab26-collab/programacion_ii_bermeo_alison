from django.urls import path

from views.autor_views import (
    autor_create,
    autor_delete,
    autor_list,
    autor_update,
)

urlpatterns = [
    path('autores/', autor_list, name='autor_list'),
    path('autores/crear/', autor_create, name='autor_create'),
    path('autores/editar/<int:pk>/', autor_update, name='autor_update'),
    path('autores/eliminar/<int:pk>/', autor_delete, name='autor_delete'),
]
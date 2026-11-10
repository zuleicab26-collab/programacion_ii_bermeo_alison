from django.urls import path

from catalogo.views import create_libro, libro_list, delete_libro, update_libro

urlpatterns = [
    path('libros/', libro_list, name='libro_list'),
    path('libros/crear/', create_libro, name='create_libro'),
    path('libros/editar/<int:pk>/', update_libro, name='update_libro'),
    path('libros/eliminar/<int:pk>/', delete_libro, name='delete_libro'),
]
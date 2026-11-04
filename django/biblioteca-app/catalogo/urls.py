from django.urls import path

from views.categoria_views import categoria_create, categoria_list


urlpatterns = [
    path('', categoria_list, name='categoria_list'),
    path('categorias/nueva/', categoria_create, name='categoria_create'),
]
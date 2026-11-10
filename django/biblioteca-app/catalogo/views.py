from django.shortcuts import render

from views.home_views import home_view
from views.categoria_views import (
    categoria_create,
    categoria_delete,
    categoria_list,
    categoria_update,
)
from views.libro_views import (
    create_libro,
    delete_libro,
    libro_list,
    update_libro,
)

from django.urls import path
from catalogo.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
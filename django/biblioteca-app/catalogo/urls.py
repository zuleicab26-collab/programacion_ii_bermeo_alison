from django.urls import include, path

urlpatterns = [
    path('', include('url.home_urls')),
    path('catalogo/', include('url.categoria_urls')),
    path('catalogo/', include('url.libro_urls')),
    path('catalogo/', include('url.autor_urls')),
    path('cuentas/', include('url.authentication_urls')),
]

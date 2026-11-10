from django.urls import include, path


urlpatterns = [
    path('', include('url.home_urls')),
    path('categoria/', include('url.libro_urls')),
    path('catalogo/', include('url.categoria_urls')),
    path('catalogo/', include('url.libro_urls')),
]
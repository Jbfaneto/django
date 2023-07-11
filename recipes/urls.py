from django.contrib import admin
from django.urls import path
from .views import home, contatos, sobre


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contatos/', contatos),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pagina_1', views.pagina_1, name='pagina_1'),
    
]
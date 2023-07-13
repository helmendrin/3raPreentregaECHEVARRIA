from django.urls import include, path
from Home import views

urlpatterns = [
    path('menu/', views.mostrar_menu, name='mostrar_menu'),
    path('tomar_pedido/<int:mesa_id>/', views.tomar_pedido, name='tomar_pedido'),
    path('gestionar_mesas/', views.gestionar_mesas, name='gestionar_mesas'),
    path('', include('Home.urls')),
   
]



from AppGoldenCafe import views
from django.urls import path




urlpatterns = [
    #URL de la pagina principal:
    path('', views.inicio, name='padre'),
    path('homepage/', views.homepage, name='homepage'),

    #URLs de las vistas de cada clase:
    path('clientes/', views.cliente, name='clientes'),
    path('pedidos/', views.pedido, name='pedidos'),
    path('sucursales/', views.sucursal, name='sucursales'),
    path('editar_cliente/<str:nombre>/', views.editar_cliente, name='editar_cliente'),
    path('editar_pedido/<str:tipo_cafe>/', views.editar_pedido, name='editar_pedido'),
    path('editar_sucursal/<str:barrio>/', views.editar_sucursal, name='editar_sucursal'),
    path('aboutme/', views.about_me, name='aboutme'),

]


 
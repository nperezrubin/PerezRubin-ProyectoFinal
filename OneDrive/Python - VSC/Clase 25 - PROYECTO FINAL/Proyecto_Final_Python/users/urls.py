from users import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('registro/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='AppGoldenCafe/padre.html'), name="Logout"),
    path('edit/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_pass/', views.CambiarContraseña.as_view(), name="CambiarPass"),
]

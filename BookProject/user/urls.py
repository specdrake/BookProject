from django.urls import path
from .views import set_csrf_token, LoginView, CheckAuth




urlpatterns = [
path('set-csrf/', set_csrf_token, name='set-CSRF'),
path('login/', LoginView, name='login'),
path('test-auth/', CheckAuth.as_view(), name='test-Auth')
]

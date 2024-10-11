from django.urls import path
from . import views

app_name = "c_admin"


urlpatterns = [
    path('', views.custom_admin, name='custom_admin'),
    path('login/', views.sign_in, name='signin'),
]
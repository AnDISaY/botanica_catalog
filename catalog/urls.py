from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('submit/', views.submit, name='submit'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('<str:project_slug>/<int:pk>/', views.villa_detail, name='villa_detail'),
]
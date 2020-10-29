from django.urls import path, include
from first_project import views


urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('formpage', views.form_name_view, name='form_name'),
    path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),


]

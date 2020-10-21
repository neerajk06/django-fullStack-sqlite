from django.urls import path, include
from first_project import views

urlpatterns = [
    path('', views.index, name='index'),

]

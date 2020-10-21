from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Hello I am from Views.py - coming from first_project !"}
    return render(request, 'first_project/index.html', context=my_dict)

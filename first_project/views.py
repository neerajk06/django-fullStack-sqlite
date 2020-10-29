from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# import the models
from first_project.models import Topic, Webpage, AccessRecord
from first_project.user_form import NewUser
from first_project.forms import UserForm, UserProfileInfoForm

# for login functionality

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

# Create your views here.
def index1(request):
    # get data from db using models
    webpage_list = AccessRecord.objects.order_by('date')
    # assigning data to dictionary
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_project/index1.html', context=date_dict)


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation success")
            # to print form info when clicked button
            print("Name- " + form.cleaned_data['name'])

    return render(request, 'first_project/form_page.html', {'form': form})


def users_view(request):
    # this code is used when fetch from db and return back
    # user_list = User.Objects.order_by('first_name')
    # user_dict = {"users": user_list}
    # return render(request, "first_project/users.html", context=user_dict)

    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error in form')

    return render(request, 'first_project/users.html', {'form': form})


'''
def index(request):
    context_dict = {'text': 'hello world', 'number': 500}
    return render(request, 'first_project/index.html', context_dict)
'''


def other(request):
    return render(request, 'first_project/other.html')


def relative(request):
    return render(request, 'first_project/relative_url_template.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_project/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})





def index(request):
    return render(request, 'first_project/indexe.html')


# login functionaliy
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not Active")

        else:
            print("Someone tried to login and failing")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'first_project/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in , Nice!")

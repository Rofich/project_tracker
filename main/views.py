from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegistrationForm, ProjectForm
from .models import Project

def index(request):
    return render(request, 'index.html')


def projects(request):
    project_list = Project.objects.filter(user=request.user)
    return render(request, 'my_projects.html', {'project_list': project_list})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my-projects')
    else:
        form = ProjectForm()
    return render(request, 'add-project.html', {'form': form})

def tasks(request):
    return render(request, 'my_tasks.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form.add_error('username', 'Неверные данные')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'],
                                password=form.data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form.add_error('username', 'Данные введены неверно')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

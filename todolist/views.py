from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import datetime
from todolist.form_todolist import TaskForm
from django.contrib.auth import logout
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = None

    if request.user.is_authenticated:
        username = request.user.get_username()
    
    # data_todolist = Task.objects.filter(user = request.user)
    context = {
        # 'list_todo': data_todolist,
        'username': username,
        'user' : request.user,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            Task.objects.create(title=title, description=description, date=datetime.datetime.now(), user=request.user)
            return redirect('todolist:show_todolist')
    
    else:
        form = TaskForm()
 
    context = {'form':form}
    return render(request, 'create-task.html', context)

@login_required(login_url='/todolist/login/')
def status(request, id):
    task = Task.objects.get(id = id)
    task.finished = not(task.finished)
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json_by_id(request):
    task = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description, date=datetime.date.today(), finished=False, user=request.user)

        output = {
            'pk':task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'finished':task.finished,
                'date':task.date,
            }
        }

        return JsonResponse(output)
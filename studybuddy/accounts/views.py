from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Course
from django.contrib.auth.models import User
from accounts.models import Course
from .forms import CreateUserForm
from .forms import EnrollForm
from django.contrib.auth import authenticate,login,logout
from django.http import FileResponse
import os
def home(request):
    Courses = Course.objects.all()

    return render(request, "accounts/mycourse.html", {'Courses': Courses})

    #return render(request,'accounts/mycourse.html')

def redirecthome(request):
    return render(request,'accounts/home_lr.html')
def logouttohome(request):
    return render(request,'accounts/home_lr.html')


def loginpage(request):
    if request.method == 'POST':
       username= request.POST.get('username')
       password=request.POST.get('password')
       user = authenticate(request, username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('home')
    context ={}
    return render(request,'accounts/login.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')

def javacourseview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/java_course.html')
    else:
        return redirect('login')
def cppcourseview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/cpp_course.html')
    else:
        return redirect('login')

def pythoncourseview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/python_course.html')
    else:
        return redirect('login')
def aboutview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/about.html')
    else:
        return redirect('login')

def quizjavaview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/quiz_java.html')
    else:
        return redirect('login')
def quizpythonview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/quiz_python.html')
    else:
        return redirect('login')
def quizcppview(request):
    if request.user.is_authenticated:
        return render(request,'accounts/quiz_cpp.html')
    else:
        return redirect('login')

def availcourseview(request):
    if request.user.is_authenticated:
        Courses = Course.objects.all()
        return render(request, "accounts/availablecourses.html", {'Courses': Courses})
        #return render(request,'accounts/availablecourses.html')
    else:
        return redirect('login')
def viewbookspage(request):
    if request.user.is_authenticated:
        Courses = Course.objects.all()
        return render(request, "accounts/viewbooks.html", {'Courses': Courses})
    else:
        return redirect('login')
def javabookview(request):
    if request.user.is_authenticated:
        filepath = os.path.join('static', 'javabook.pdf')
        return FileResponse(open(filepath, 'rb'), content_type = 'application/pdf')
        #return render(request,'accounts/viewbooks.html')
    else:
        return redirect('login')
def pythonbookview(request):
    if request.user.is_authenticated:
        filepath = os.path.join('static', 'pythonbook.pdf')
        return FileResponse(open(filepath, 'rb'), content_type = 'application/pdf')
        #return render(request,'accounts/viewbooks.html')
    else:
        return redirect('login')
def cppbookview(request):
    if request.user.is_authenticated:
        filepath = os.path.join('static', 'Cppbook.pdf')
        return FileResponse(open(filepath, 'rb'), content_type = 'application/pdf')
        #return render(request,'accounts/viewbooks.html')
    else:
        return redirect('login')
def viewenrollpage(request):
    if request.user.is_authenticated:
        form = EnrollForm(request.POST or None)
        if request.method == 'POST':
                form = EnrollForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('home')
        return render(request,'accounts/enrollcourse.html', {'form':form})
    else:
        return redirect('login')







  

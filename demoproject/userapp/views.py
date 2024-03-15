from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def index(request):
    return render(request, 'home.html')

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_details')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def user_details(request):
    users = User.objects.all()
    return render(request, 'user_details.html', {'users': users})

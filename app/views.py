from django.shortcuts import render
from .models import User


def home(request):
    return render(request, 'user/home.html')


def users(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        if name and age:
            new_user = User(name=name, age=age)
            new_user.save()
    context = {
        'users': User.objects.all()
    }
    return render(request, 'user/users.html', context)

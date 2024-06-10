from django.contrib.auth import (authenticate,
                                 login,
                                 logout)
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html')


def user_login(request):
    # Process login form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

        return render(request, 'login.html',
                      {'error': 'Nom d\'utilisateur ou mot de passe incorrect'})

    # Display login page
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('index')

from django.shortcuts import redirect, render
from django.contrib.auth import login

from core.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # cria a sessão do usuário. Define request.user para  esse usuário. Cria coockie da sessão.
            return redirect('edu:home')
    else:
        form = SignUpForm() 
    # Lógica para lidar com o cadastro de usuários
    return render(request, 'edu/signup.html', {'form': form})

def login_view(request):
    # Lógica para lidar com o login de usuários
    return render(request, 'edu/login.html')

def logout_view(request):
    # Lógica para lidar com o logout de usuários
    return render(request, 'edu/logout.html')
# Create your views here.

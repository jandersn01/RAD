from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.utils.http import url_has_allowed_host_and_scheme 
from core.forms import SignUpForm , LoginForm
from django.http import HttpResponseNotAllowed

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # cria a sessão do usuário. Define request.user para  esse usuário. Cria coockie da sessão.
            return redirect('blog:home')
    else:
        form = SignUpForm() 
    # Lógica para lidar com o cadastro de usuários
    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next' ,'') or request.GET.get('next', '')
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            
            return redirect('blog:home')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form' : form})

def logout_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    logout(request)
    # Lógica para lidar com o logout de usuários
    return redirect('core:login')

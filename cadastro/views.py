from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import UsuarioForm
#from django.http import HttpResponse

@csrf_protect
def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro/cadastro.html', {'form': form})


#def home(request):
 #   return HttpResponse("Bem-vindo à página inicial!")
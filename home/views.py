from home.models import Opinion
from home.forms import OpinionForm
from django.forms.forms import Form
from django.utils import timezone
from datetime import datetime 
from django.shortcuts import redirect, render
from django.http import HttpResponse

def horario_dieteica():
    actual = timezone.now()
    if actual.strftime("%A") != "Sundary":
        hora_inicio_mañana = datetime.strptime("08:00:00", "%X").time()
        hora_fin_mañana = datetime.strptime("12:00:00", "%X").time()
        hora_inicio_tarde = datetime.strptime("17:00:00", "%X").time()
        hora_fin_tarde = datetime.strptime("20:00:00", "%X").time()
        hora_actual = datetime.now().time()
        if hora_actual > hora_inicio_mañana and hora_actual < hora_fin_mañana:
            return True
        else:
            if hora_actual > hora_inicio_tarde and hora_actual < hora_fin_tarde:
                return True
            else:
                return False
    else:
        return False

def horario_nutricionista():
    actual = timezone.now()
    if actual.strftime("%A") in ["Monday","Wednesday","Friday"]:
        hora_inicio_tarde = datetime.strptime("17:00:00", "%X").time()
        hora_fin_tarde = datetime.strptime("19:00:00", "%X").time()
        hora_actual = datetime.now().time()
        return hora_actual > hora_inicio_tarde and hora_actual < hora_fin_tarde
    else:
        return False

def home(request):
    dietetica_abierto = horario_dieteica()
    nutricionista_abierto = horario_nutricionista()
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            publicacion = True
        return redirect('home')
    else:
        form = OpinionForm()
    opiniones = sorted(Opinion.objects.all(),key=lambda o:len(o.contenido))
    return render(
        request,
        'home/inicio.html',
        {
        'titulo' : 'Qumara Aymara - Inicio',
        'dietetica' : dietetica_abierto,
        'nutricionista' : nutricionista_abierto,
        'form' : form,
        'opiniones' : opiniones,        
        }
    )


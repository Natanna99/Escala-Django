import datetime
from django.db.models.fields import DateField
from django.forms.widgets import DateInput
from Escala.settings import DATE_INPUT_FORMATS
from django.shortcuts import redirect, render
from django.urls.base import reverse
from datetime import date, datetime
from .models import *
from .forms import *
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

class home(TemplateView):
    def medico(request):
        return render(request, "paginas/homes.html", {"tipo": "Medico"})

    def posto(request):
        return render(request, "paginas/homes.html", {"tipo": "posto"})

    def folga(request):
        return render(request, "paginas/homes.html", {"tipo": "folga"})

    def escala(request):
        return render(request, "paginas/homes.html", {"tipo": "escala"})


def cadastrar_medicos(request):
    if request.method == 'GET':    
        form = Cadastrar_Medico_Form
        return render(request, 'paginas/cadastrar_medico.html', {'formulario': form})

    elif request.method == 'POST':     
        medico = Medico()
        medico.nome = request.POST['nome']
        medico.sobrenome = request.POST['sobrenome']
        medico.data_admissao = request.POST['data_admissao']

        medico.save()

        return redirect(reverse('lista_medico'))


def lista_medico(request):
    lista= Medico.objects.all()
    return render(request, "paginas/lista_medico.html", {"lista": lista})

def atualizar_medico(request):
    medico_id = request.GET.get('id')
    if medico_id:
        medico = Medico.objects.get(id= medico_id)
        print(medico.data_admissao)
        
        
        return render(request, 'paginas/cadastrar_medico.html', {'medico':medico, "data": medico.data_admissao.strftime('%d/%m/%Y')})
    
    M_id= request.POST.get('medico_id')
    if M_id:
       medico = Medico.objects.get(id= M_id)
       medico.nome = request.POST['nome']
       medico.sobrenome = request.POST['sobrenome']
       medico.data_admissao = request.POST[date('data_admissao')]
       medico.save()

       return redirect(reverse('lista_medico'))

def cadastrar_posto(request):
    if request.method == 'GET':    
        form = Cadastrar_Posto_Form
        return render(request, 'paginas/cadastrar_posto.html', {'formulario': form})

    elif request.method == 'POST':     
        posto = Posto()
        posto.nome_posto = request.POST['nome']
        posto.endereco= request.POST['endereco']
        posto.save()

        return redirect(reverse('lista_posto'))

def lista_posto(request):
    lista= Posto.objects.all()
    return render(request, "paginas/lista_posto.html", {"lista": lista})

def atualizar_posto(request):
    posto_id = request.GET.get('id')
    if posto_id:
        posto = Posto.objects.get(id= posto_id)
        
        return render(request, 'paginas/cadastrar_posto.html', {'posto':posto})
        
    P_id= request.POST.get('posto_id')
    if P_id:
       posto = Posto.objects.get(id= P_id)
       posto.nome_posto = request.POST['nome']
       posto.endereco = request.POST['endereco']
       posto.save()

       return redirect(reverse('lista_posto'))

def cadastrar_folga(request):
    if request.method == 'GET':    
        form = Cadastrar_Folga_Form
        return render(request, 'paginas/cadastrar_posto.html', {'formulario': form})

    elif request.method == 'POST':     
        posto = Posto()
        posto.nome_posto = request.POST['nome']
        posto.endereco= request.POST['endereco']
        posto.save()

        return redirect(reverse('lista_posto'))

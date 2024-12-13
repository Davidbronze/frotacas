from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db import transaction
from .models import Veiculo, Viagem, Revisao, Combustivel


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class MyHomeView(ListView):
    model = Veiculo
    template_name="home.html"

    def get_queryset(self, **kwargs):
        veiculos = Veiculo.objects.all()
        return veiculos
        



def setTripView(request):
    option = request.GET
    veiculos = Veiculo.objects.all()
    selected_veiculo = veiculos.get(veiculo_nome=option.get('veiculo_nome'))
    selected_trip = Viagem.objects.filter(veiculo_id=selected_veiculo.id).last()
    revisao = Revisao.objects.filter(veiculo_id=selected_veiculo.id).last()
    combustivel = Combustivel.objects.filter(veiculo_id=selected_veiculo.id).last()
    now = timezone.now()
    interval = revisao.revisao_data - now
    return render(request, 'set_trip.html', {'selected_trip':selected_trip, 'veiculos': veiculos,
     'selected_veiculo':selected_veiculo, 'revisao':revisao,'now':now, 'interval':interval,
     'combustivel':combustivel})


def saveTripView(request):
    if request.method == "POST":
        dados = request.POST
        veiculos = Veiculo.objects.all()
        veiculo_instance = Veiculo.objects.get(id=dados['veiculo'])
        selected_veiculo = veiculo_instance.veiculo_nome
        selected_trip = Viagem.objects.filter(viagem_destino=dados['destino']).last()
        user_instance = User.objects.get(id=dados['user'])
        combustivel = Combustivel.objects.filter(veiculo_id=veiculo_instance.id).last()        
        trip = Viagem(veiculo=veiculo_instance, usuario=user_instance, viagem_destino=dados['destino'],
            viagem_datasaida=dados['start_date'], viagem_kmsaida=dados['start_km'],
            viagem_dataret=dados['end_date'], viagem_kmret=dados['end_km'])
        
        combust = Combustivel(veiculo=veiculo_instance, veiculo_combust=dados['combustivel'])

        try:
            with transaction.atomic():
                trip.save()
                combust.save()

            return render(request, 'set_trip.html',{'selected_trip':selected_trip,'veiculos':veiculos,
            'selected_veiculo': veiculo_instance, 'veiculo_combust': dados['combustivel']})

        except Exception as e:
            print(e)
            return render(request, 'erro.html', {'erro': str(e)})


        return render(request, 'set_trip.html',{'selected_trip':selected_trip,'veiculos':veiculos,
            'selected_veiculo': veiculo_instance, 'veiculo_combust': dados['combustivel']})




def veicule_list(request):
    veiculos=Veiculo.objects.all()
    return render(request, 'home.html', {'veiculos': veiculos})


def makeQuery():
    veiculos=1


def send_register(request):
    if request.method == "POST":
        veiculo=a
        usuario=b
        viagem_destino=c
        viagem_datasaida=d
        viagem_kmsaida=1
        viagem_dataret=f
        viagem_kmret=1
from django.db import models
from django.contrib.auth.models import User


class Veiculo(models.Model):
	veiculo_nome=models.CharField(max_length=30)
	veiculo_ofplaca=models.CharField(max_length=9)
	veiculo_instalplaca=models.CharField(max_length=9)
	veiculo_cartao=models.CharField(max_length=16)
	veiculo_revinterval=models.IntegerField(default=12)
	veiculo_combust=models.IntegerField(default=12)

	def __str__(self):
		return self.veiculo_nome


class Viagem(models.Model):
	veiculo=models.ForeignKey(Veiculo, on_delete=models.RESTRICT)
	usuario=models.ForeignKey(User, on_delete=models.RESTRICT)
	viagem_destino=models.CharField(max_length=200)
	viagem_datasaida=models.DateTimeField("data published")	
	viagem_kmsaida=models.IntegerField(default=0)
	viagem_dataret=models.DateTimeField("data published")
	viagem_kmret=models.IntegerField(default=0)

	def __self__(self):
		return self.viagem_destino



class Revisao(models.Model):
	veiculo=models.ForeignKey(Veiculo, on_delete=models.RESTRICT)
	revisao_data=models.DateTimeField("data published")

	def __self__(self):
		return self.veiculo



class Combustivel(models.Model):
	veiculo=models.ForeignKey(Veiculo, on_delete=models.RESTRICT)
	veiculo_combust=models.IntegerField(default=12)
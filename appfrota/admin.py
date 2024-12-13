from django.contrib import admin
from .models import Veiculo, Viagem, Revisao, Combustivel


admin.site.register(Veiculo)
admin.site.register(Viagem)
admin.site.register(Revisao)
admin.site.register(Combustivel)

# Register your models here.

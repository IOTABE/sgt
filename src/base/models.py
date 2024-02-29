from django.db import models


class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    # Outros campos de informações do motorista

    def __str__(self):
        return self.nome
    

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    odometro = models.IntegerField(default=0)
    # Outros campos de informações do veículo

    def __str__(self):
        return self.placa


class Setores(models.Model):
    setor = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)

    def __str__(self):
        return self.setor
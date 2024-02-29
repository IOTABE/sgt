from django.db import models
from base.models import Motorista, Veiculo, Setores

TIPO = [
        ('E', 'EXTERNA'),
        ('I', 'INTERNA')
        ]


class Viagens(models.Model):
    horariosolicitado = models.DateTimeField(verbose_name='Data solicitação',)
    dataatendimento = models.DateField(verbose_name="Atendido em", blank=True)
    dataagendamento = models.DateField(verbose_name='Agendado para')
    servidor = models.CharField(verbose_name='Servidor', max_length=100)
    setor = models.ForeignKey(Setores, on_delete=models.CASCADE, verbose_name='Setor',default=0)
    tiposolicitacao = models.CharField(verbose_name='Tipo Solicitacao',max_length=1,choices=TIPO)
    retorno = models.DateTimeField(verbose_name='Retorno', blank=True )
    itinerario = models.TextField(max_length=500, verbose_name='Itinerário')
    motorista = models.ForeignKey( Motorista, on_delete=models.CASCADE, verbose_name='Motorista', blank=True)
    veiculo = models.ForeignKey( Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo', blank=True)
    kminicial = models.IntegerField(verbose_name="Km Saída", blank=True)
    kmfinal = models.IntegerField(verbose_name='Km chegada', blank=True)
    observacoes = models.TextField(verbose_name="Observações", max_length=500, blank=True)

    def __str__(self):
        return self.servidor

from django.db import models
from pessoas.models import Pessoas

class Contas(models.Model):
    idConta = models.AutoField(primary_key=True)
    idPessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    saldo = models.FloatField()
    limiteSaqueDiario = models.FloatField()
    flagAtivo = models.BooleanField()
    tipoConta = models.IntegerField()
    dataCriacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.idConta

    class Meta:
        verbose_name_plural = "Contas"
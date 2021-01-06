from django.db import models

class Pessoas(models.Model):
    idPessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    dataNascimento = models.DateField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Pessoas'

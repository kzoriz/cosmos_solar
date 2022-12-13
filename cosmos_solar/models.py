from django.db import models

# Create your models here.


class SobreNos(models.Model):

    title1 = models.CharField(verbose_name="Título", blank=True, max_length=255)
    title2 = models.CharField(verbose_name="Título", blank=True, max_length=255)
    text = models.TextField(verbose_name="Texto", blank=True)

    def __str__(self):
        return "Sobre Nós: Sessão 1"

    class Meta:
        verbose_name_plural = "Sobre Nós"

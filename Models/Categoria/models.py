from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=80)

    def __str__(self):
        return self.categoria

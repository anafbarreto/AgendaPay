from django.db import models
from decimal import Decimal

class Agendamento(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField()
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=100)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Converte valor_pagamento para inteiro antes de salvar
        self.valor_pagamento = int(self.valor_pagamento)
        super().save(*args, **kwargs)

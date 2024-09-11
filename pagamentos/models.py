from django.db import models
from decimal import Decimal, ROUND_HALF_UP

class Agendamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField()
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=100)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)

    """def save(self, *args, **kwargs):
        if self.valor_pagamento is not None:
           self.valor_pagamento = Decimal(int(self.valor_pagamento))
        super().save(*args, **kwargs)"""

  
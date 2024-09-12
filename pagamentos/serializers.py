from rest_framework import serializers
from .models import Agendamento
from decimal import Decimal, ROUND_DOWN

class AgendamentoSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True) # receive only decimal values in valor_pagamento
    
    class Meta:
        model = Agendamento
        fields = '__all__'

    def to_internal_value(self, data): # convert to integer
        if 'valor_pagamento' in data:
            valor_decimal = Decimal(data['valor_pagamento']).quantize(Decimal('1'), rounding=ROUND_DOWN)
            data['valor_pagamento'] = valor_decimal.to_integral_value()  
        return super().to_internal_value(data)

    def to_representation(self, instance): # personalize the response 
        representation = super().to_representation(instance)
        representation['valor_pagamento'] = int(instance.valor_pagamento)
        return representation

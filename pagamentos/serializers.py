from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer): # convert to json
    class Meta:
        model = Agendamento
        fields = '__all__'
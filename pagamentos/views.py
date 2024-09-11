from rest_framework import viewsets
from .models import Agendamento
from .serializers import AgendamentoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet): # the ModelViewSet class handles all CRUD operations in a single class and a single route
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

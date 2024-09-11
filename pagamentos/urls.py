from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AgendamentoCreateView

router = SimpleRouter(trailing_slash=False) # add / at the end URL
router.register('agendamentos/', AgendamentoCreateView) # define URL

urlpatterns = [
    path('', include(router.urls)), 
]

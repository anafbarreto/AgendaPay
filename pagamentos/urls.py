from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgendamentoViewSet

router = DefaultRouter()  # CRUD complete 
router.register(r'agendamentos', AgendamentoViewSet)  

urlpatterns = [
    path('', include(router.urls)),  # routes all URLs from the router
]

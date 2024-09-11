from rest_framework.test import APITestCase
from rest_framework import status
from .models import Agendamento
from django.urls import reverse

# creates agendamento for use in tests
class AgendamentoTests(APITestCase): 
    def setUp(self):
        self.agendamento = Agendamento.objects.create(
            data_pagamento='2024-09-15',
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia='ativo',
            agencia=1234,
            conta=56789,
            valor_pagamento=1234.56
        )
        self.url = reverse('agendamento-list')  
    
    # verifies that the  listing is working and that the number of agendamentos returned is correct
    def test_list_agendamentos(self): 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    # checks whether the creation of a new agendamento is working and that the total number increases as expected
    def test_create_agendamento(self): 
        data = {
            "data_pagamento": "2024-10-01",
            "permite_recorrencia": False,
            "quantidade_recorrencia": 0,
            "intervalo_recorrencia": 0,
            "status_recorrencia": "concluído",
            "agencia": 1234,
            "conta": 56789,
            "valor_pagamento": 1500.75
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agendamento.objects.count(), 2)  

    # validates that the query for a specific agendamento  is working and that the data returned is correct
    def test_retrieve_agendamento(self): 
        url = reverse('agendamento-detail', kwargs={'pk': self.agendamento.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.agendamento.id)

    # check the update of a agendamento is working and returning correctly
    def test_update_agendamento(self):
        url = reverse('agendamento-detail', kwargs={'pk': self.agendamento.id})
        data = {
            "data_pagamento": "2024-11-01",
            "permite_recorrencia": False,
            "quantidade_recorrencia": 0,
            "intervalo_recorrencia": 0,
            "status_recorrencia": "concluído",
            "agencia": 1234,
            "conta": 56789,
            "valor_pagamento": 1500.75
    }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.agendamento.refresh_from_db()  # atualize the object from the database
        self.assertEqual(self.agendamento.data_pagamento.strftime('%Y-%m-%d'), '2024-11-01') # convert the date to string because its the returned JSON

    # validates if the agendamento has been deleted
    def test_delete_agendamento(self):
        url = reverse('agendamento-detail', kwargs={'pk': self.agendamento.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agendamento.objects.count(), 0)  



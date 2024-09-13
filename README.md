# AgendaPay
API for managing payment schedules, developed using Python with Django and Django REST Framework (DRF). The API allows you to perform CRUD operations (create, list, query, update and delete) on payment schedules. 


### Index
* [Response](#application-result)
* [Project description](#project-description)
* [Technologies used](#technologies-used)
* [Tests](#tests)
* [Project execution](#project-execution)
* [Test execution](#test-execution)
* [Continuous Integration](#continuous-integration)
* [Thanks](#thanks) 



### Application result
```
{
  "id": 68,
  "data_pagamento": "2024-09-15",
  "permite_recorrencia": true,
  "quantidade_recorrencia": 5,
  "intervalo_recorrencia": 30,
  "status_recorrencia": "ativo",
  "agencia": 1234,
  "conta": 56789,
  "valor_pagamento": 99
}
``` 


### Project description
* Create: Allows you to create new payment schedules.
* List: Displays a list of all created schedules.
* Query: Retrieves a specific schedule based on its ID.
* Update: Updates the data of an existing schedule based on its ID.
* Delete: Removes an existing schedule from the database based on its ID.


### Technologies used
* Django: Web framework used to build the project structure and backend.
* Django REST Framework (DRF): Django extension that makes it easy to create RESTful APIs.
* SQLite: Database used by default by Django for data storage.
* ViewSets: ViewSets were used to abstract the CRUD logic into a single class, making the code simpler and more organized.
* APITestCase: Automated tests implemented to ensure the API works as expected.

### Tests
Code and test coverage: 92%** (Coverage Report) <br>
 ** The report can be found in the Github Actions.

### Project Execution
Make sure you have Python 3.8+ installed on your system.

1. Clone the repository: <br>
```
git clone https://github.com/anafbarreto/AgendaPay.git
cd AgendaPay
```
2. Create a virtual environment (optional, but recommended):
```
python -m venv .venv
```
3. To activate:
```
.venv\Scripts\activate 
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Perform database migrations:
```
python manage.py migrate
```
6. Run the server:
```
python manage.py runserver
```
7. The API will be available at http://127.0.0.1:8000/api/agendamentos/. <br>
You can use tools like Postman, or Thunder Client - a very practical and efficient VS Code extension. <br>
Note: to execute PUT or DELETE you must enter the ID at http://127.0.0.1:8000/api/agendamentos/ID/.


#### Examples
Method: POST <br>
URL: /api/agendamentos/ <br>
Request Body: <br>
```
{
  "data_pagamento": "YYYY-MM-DD",
  "permite_recorrencia": true,
  "quantidade_recorrencia": 5,
  "intervalo_recorrencia": 30,
  "status_recorrencia": "ativo",
  "agencia": 1234,
  "conta": 56789,
  "valor_pagamento": 1500.50
}
```
Method: GET <br>
URL: /api/agendamentos/ <br>
Or URL: /api/agendamentos/id/ <br>
Response: 
```
{
  "id": 1,
  "data_pagamento": "2024-09-15",
  "permite_recorrencia": true,
  "quantidade_recorrencia": 5,
  "intervalo_recorrencia": 30,
  "status_recorrencia": "ativo",
  "agencia": 1234,
  "conta": 56789,
  "valor_pagamento": 1500
}
```


Method: PUT <br>
URL: /api/agendamentos/id/ <br>
Request Body: <br>
```
{
  "data_pagamento": "YYYY-MM-DD",
  "permite_recorrencia": false,
  "quantidade_recorrencia": 0,
  "intervalo_recorrencia": 0,
  "status_recorrencia": "concluído",
  "agencia": 1234,
  "conta": 56789,
  "valor_pagamento": 1500
}
```

Method: DELETE <br>
URL: /api/agendamentos/id/ <br>
Status: 204 No Content <br>


### Test execution
Automated tests were implemented using the `rest_framework.test.APITestCase library`.

1. Run the command:
```
python manage.py test
```
This will run all tests located in the `tests.py` file and return the test results to the console.


### Continuous Integration
This project uses GitHub Actions to perform Continuous Integration (CI). Whenever a change is made to the main branch, whether via push or pull request, automated tests are run to ensure that the code continues to work correctly. <br>
The CI configuration file is located in the `.github/workflows/ directory`.


### Thanks!!
![catdev](https://github.com/anafbarreto/Desafio/assets/44984838/87f17484-6a56-4b34-b52e-c3ecb980edd0)




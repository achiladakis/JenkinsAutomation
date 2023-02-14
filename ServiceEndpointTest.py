######
## Script Execution pytest -v 
## -v = Verbose
######

import pytest
import requests

## Definiere Endpoint
endpoint = "https://petstore.swagger.io/"

response = requests.get(endpoint)

##Test1 - Prüfe Endpoint (Allgemein) https://petstore.swagger.io/
def test_calling_endpoint():
    response = requests.get(endpoint)
    assert response.status_code == 200
    pass

##Test2 /pet/findByStatus
def test_calling_findbystatus():
    response = requests.get(endpoint + "v2/pet/findByStatus?status=sold")
    assert response.status_code == 200
    pass

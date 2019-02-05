"""
Adds a person using the OpenMRS REST API
"""
import requests
import json

URL_PERSON = 'http://192.168.0.200:8085/openmrs/ws/rest/v1/person'
PAYLOAD = {'gender': 'M', 'names': [{'givenName': 'Egberto',
    'familyName': 'Torres'}]}
HEADERS = {'content-type': 'application/json'}
DATA = json.dumps(PAYLOAD)
REQ = requests.post(URL_PERSON, DATA, auth=('admin', 'test'),
    headers=HEADERS)
PERSON_UUID = json.loads(REQ.text)['uuid']
LOCATION_UUID = "68c5401a-0d4d-45ac-b908-a9ede758df6f"
IDENTIFIER_UUID = "820299d2-438a-4b8e-9c79-a26f52089e73"

URL_PATIENT = 'http://192.168.0.200:8085/openmrs/ws/rest/v1/patient'
PATIENT_PAYLOAD = {"person": PERSON_UUID,
    "identifiers": [{"identifier":"18080300",
    "identifierType":IDENTIFIER_UUID,
    "location":LOCATION_UUID,
    "preferred":True}]}
DATA = json.dumps(PATIENT_PAYLOAD)
REQ = requests.post(URL_PATIENT, DATA, auth=('admin', 'test'),
    headers=HEADERS)

print REQ.text

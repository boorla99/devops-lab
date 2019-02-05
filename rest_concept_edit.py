"""
Edit Concepts through OpenMRS REST API
"""
import requests
import json
import unicodecsv


HEADERS = {'content-type': 'application/json'}

SERVER = 'http://192.168.1.200:8085/'


URL_CONCEPT = '%sopenmrs/ws/rest/v1/concept' % SERVER
REQ = requests.get(URL_CONCEPT, auth=('admin', 'test'), headers=HEADERS)
CONCEPT = json.loads(REQ.text)['results']
CONCEPT_DICTIONARY = {}
for elem in CONCEPT:
    CONCEPT_DICTIONARY[elem['display']] = elem['uuid']

FILENAME = 'diccionario_postulante.csv'
LINES = unicodecsv.reader(open(FILENAME), encoding='utf-8')

URL_CONCEPT = '%sopenmrs/ws/rest/v1/concept' % SERVER

for line in LINES:
    concept_payload = {
        "names": [
            {"name": line[0], "locale": "es",
                "conceptNameType": "FULLY_SPECIFIED"},
            {"name": line[1], "locale": "es",
                "conceptNameType": "SHORT"},
            ],
        "set": True
    }
    data = json.dumps(concept_payload)
    REQ = requests.post(URL_CONCEPT, data, auth=('admin', 'test'),
        headers=HEADERS)
    print REQ.text

"""
Add concepts through CSV file through OpenMRS REST API
"""
import requests
import json
import unicodecsv


HEADERS = {'content-type': 'application/json'}

SERVER = 'http://192.168.1.200:8085/'

URL_CONCEPTCLASS = '%sopenmrs/ws/rest/v1/conceptclass' % SERVER
REQ = requests.get(URL_CONCEPTCLASS, auth=('admin', 'test'),
    headers=HEADERS)
CONCEPTCLASS = json.loads(REQ.text)['results']
CONCEPTCLASS_DIC = {}
for elem in CONCEPTCLASS:
    CONCEPTCLASS_DIC[elem['display']] = elem['uuid']

URL_CONCEPTDATATYPE = '%sopenmrs/ws/rest/v1/conceptdatatype' % SERVER
REQ = requests.get(URL_CONCEPTDATATYPE, auth=('admin', 'test'),
    headers=HEADERS)
CONCEPTDATATYPE = json.loads(REQ.text)['results']
CONCEPTDATATYPE_DIC = {}
for elem in CONCEPTDATATYPE:
    CONCEPTDATATYPE_DIC[elem['display']] = elem['uuid']

FILENAME = 'diccionario_postulante.csv'
LINES = unicodecsv.reader(open(FILENAME), encoding='utf-8')

URL_CONCEPT = '%sopenmrs/ws/rest/v1/concept' % SERVER

for line in LINES:
    concept_payload = {
        "names": [
            {"name": line[0], "locale":"es",
                "conceptNameType": "FULLY_SPECIFIED"},
            {"name": line[1], "locale":"es",
                "conceptNameType": "SHORT"},
            ],
        "datatype": CONCEPTDATATYPE_DIC[line[5]],
        "conceptClass": CONCEPTCLASS_DIC[line[4]],
        "set": True
    }
    data = json.dumps(concept_payload)
    REQ = requests.post(URL_CONCEPT, data, auth=('admin', 'test'),
        headers=HEADERS)
    print REQ.text

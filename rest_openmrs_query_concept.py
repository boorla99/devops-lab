"""
Searchs concepts UUID through CSV file using OpenMRS REST API
"""
import requests
import json
import unicodecsv


HEADERS = {'content-type': 'application/json'}

SERVER = 'http://192.168.0.200:8085/'


FILENAME = 'diccionario_postulante.csv'
LINES = unicodecsv.reader(open(FILENAME), encoding='utf-8')
CONCEPT_DIC = {}

for line in LINES:
    url_concept = '%sopenmrs/ws/rest/v1/concept?q=%s' % (SERVER,
        line[0])
    r = requests.get(url_concept, auth=('admin', 'test'),
        headers=HEADERS)
    concept = json.loads(r.text)['results']
    for elem in concept:
        CONCEPT_DIC[elem['display']] = elem['uuid']


for concept in CONCEPT_DIC:
    url_concept = '%sopenmrs/ws/rest/v1/concept/%s' % (SERVER,
        CONCEPT_DIC[concept])
    print concept, url_concept

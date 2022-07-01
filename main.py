import requests
import json
import base64
import os

huser = os.environ['HARBOR_USER']
hpass = os.environ['HARBOR_PASS']

encoded = base64.b64encode(f'{huser}:{hpass}'.encode('ascii'))

print(encoded)

with open('images.json') as json_file:
    data = json.load(json_file)

x = requests.get('https://w3schools.com/python/demopage.htm')

print(f'Basic {encoded.decode("utf-8")}')

headers={
    'accept': 'application/json',
    'authorization': f'Basic {encoded.decode("utf-8")}'
    }

response = requests.get(
    'https://harbor.airgap.angrydome.io/api/v2.0/replication/policies?page=1&page_size=10',
    headers=headers,
)

print(response.json())

images = [i['original'] for i in data]

payload = dict()

for image in images:
    registry = image.split('/')[0]
    repo_tag = '/'.join(image.split('/')[1:])
    repo = repo_tag.split(':')[0]
    tag = repo_tag.split(':')[1]

    if registry not in payload.keys():
        payload[registry] = dict()

    if repo not in payload[registry].keys():
        payload[registry][repo] = list()
    
    if tag not in payload[registry][repo]:
        payload[registry][repo].append(tag)

print(json.dumps(payload, indent=2))


new_registry = {
    "credential": {},
    "name": "eu.gcr.io",
    "type": "docker-registry",
    "url": "https://eu.gcr.io"
  }

# create_reg = requests.post(
#     'https://harbor.airgap.angrydome.io/api/v2.0/registries',
#     headers=headers,
#     json=new_registry
# )

# print(create_reg)

registries = requests.get(
    'https://harbor.airgap.angrydome.io/api/v2.0/registries?page=1&page_size=10',
    headers=headers,
)

print(json.dumps(registries.json(), indent=2))

print(payload.keys())

for reg in payload.keys():
    active_reg = [r['name'] for r in registries.json()]
    if reg not in active_reg:
        print(f'{reg} not in harbor')


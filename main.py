# """
# curl -X 'POST' \
#   'http://5.63.153.31:5051/v1/account' \
#   -H 'accept: */*' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "login": "pestov_test",
#   "email": "vlad-pestov@mail.ru",
#   "password": "123456789"
# }'
# """
#
# curl -X 'PUT' \
#   'http://5.63.153.31:5051/v1/account/1f1e922e-4163-48ba-9cf9-374dd2c5d1ca' \
#   -H 'accept: text/plain'

import pprint

import requests

url = 'http://5.63.153.31:5051/v1/account/1f1e922e-4163-48ba-9cf9-374dd2c5d1ca'
headers = {
    'accept': 'text/plain',
}
# json = {
#     "login": "pestov_test_2",
#     "email": "vlad-pestov_2@mail.ru",
#     "password": "123456789"
# }

response = requests.put(
    url=url,
    headers=headers,
)
print(response.status_code)
pprint.pprint(response.json())

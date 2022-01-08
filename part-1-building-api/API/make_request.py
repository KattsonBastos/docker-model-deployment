import requests

api_url = 'http://localhost:8000/cvd-classification'

data = {
    "age": [20],
    "weight": [80],
    "ap_hi": [125],
    "ap_lo": [80],
    "cholesterol": [1]
}

print('Data passed: ', data)

r = requests.post(url=api_url, json=data)

print('Request code status: ', r.status_code)

print(r.reason)

print(r.text)


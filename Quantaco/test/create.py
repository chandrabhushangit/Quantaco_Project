import requests

endpoint = "http://localhost:8000/customer/" 

data = {'first_name': 'test', 'last_name': 'jjj', 'date_of_birth': '2000-01-01', 'phone_number': '+91 8888678901'}
get_response = requests.post(endpoint, json=data) 
print(get_response.json())
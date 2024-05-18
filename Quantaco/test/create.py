import requests

endpoint = "http://localhost:8000/customer/" 

data = {'first_name': 'Chandra', 'last_name': 'Mishra', 'date_of_birth': '1990-01-01', 'phone_number': '1234567890'}
get_response = requests.post(endpoint, json=data) 
print(get_response.json())
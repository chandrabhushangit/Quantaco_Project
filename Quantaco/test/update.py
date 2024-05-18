import requests

endpoint = "http://localhost:8000/customer/2/update/" 

data = {'first_name': 'Bob', 'last_name': 'Brown', 'date_of_birth': '1978-12-11', 'phone_number': '4444444444'}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())
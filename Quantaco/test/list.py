import requests

endpoint = "http://localhost:8000/customer/" 

get_response = requests.get(endpoint) 
print(get_response.json())
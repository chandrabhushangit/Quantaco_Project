import requests

endpoint = "http://localhost:8000/customer/register/" 

data = {'first_name': 'hhhhh', 'last_name': 'jjj', 'date_of_birth': '2000-01-01', 'phone_number': '+918888678901'}
get_response = requests.post(endpoint, json=data) 

with open('hello.html', 'w', encoding='utf-8') as file:
    file.write(get_response.text)
print(get_response.text)
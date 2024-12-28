import requests

endpoint = "http://localhost:8000/updisht/api/dashboard" 

get_response = requests.get(endpoint) 
if get_response.status_code == 200:
    try:
        data = get_response.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
else:
    print(f"Request failed with status code {get_response.status_code}")
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def list():
    response = requests.get(BASE_URL)
    return response.json()

def read(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    return response.json()

def create(data):
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update(user_id, data):
    response = requests.put(f"{BASE_URL}/{user_id}", json=data)
    return response.json()

def delete(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    return {"status": response.status_code}

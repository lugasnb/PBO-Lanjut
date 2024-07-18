import requests

BASE_URL = 'http://localhost/quiz_pbo/api/customer.php'

def get_customer():
    response = requests.get(BASE_URL)
    return response.json()

def get_customer_by_id(customer_id):
    response = requests.get(f'{BASE_URL}?id={customer_id}')
    return response.json()

def create_customer(ktp, nama_customer, jk, kota):
    data = {'ktp': ktp, 'nama_customer': nama_customer, 'jk': jk, 'kota': kota}
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_customer(customer_id, ktp, nama_customer, jk, kota):
    data = {'ktp': ktp, 'nama_customer': nama_customer, 'jk': jk, 'kota': kota}
    response = requests.put(f'{BASE_URL}?id={customer_id}', json=data)
    return response.json()

def delete_customer(customer_id):
    response = requests.delete(f'{BASE_URL}?id={customer_id}')
    return response.json()

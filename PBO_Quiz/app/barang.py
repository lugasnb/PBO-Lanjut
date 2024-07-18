import requests

BASE_URL = 'http://localhost/quiz_pbo/api/barang.php'

def get_barang():
    response = requests.get(BASE_URL)
    return response.json()

def get_barang_by_id(barang_id):
    response = requests.get(f'{BASE_URL}?id={barang_id}')
    return response.json()

def get_barang_by_kode(kode_barang):  # Tambahkan fungsi ini untuk mendapatkan barang berdasarkan kode
    response = requests.get(f'{BASE_URL}?kode_barang={kode_barang}')
    return response.json()

def create_barang(kode_barang, nama_barang, harga):
    data = {'kode_barang': kode_barang, 'nama_barang': nama_barang, 'harga': harga}
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_barang(barang_id, kode_barang, nama_barang, harga):
    data = {'kode_barang': kode_barang, 'nama_barang': nama_barang, 'harga': harga}
    response = requests.put(f'{BASE_URL}?id={barang_id}', json=data)
    return response.json()

def delete_barang(barang_id):
    response = requests.delete(f'{BASE_URL}?id={barang_id}')
    return response.json()

import requests
import json

class Rental:

    def __init__(self):
        self.__id = None
        self.__kodeps = None
        self.__kdpelanggan = None
        self.__tipe_ps = None
        self.__mulai = None
        self.__selesai = None
        self.__url = "http://localhost/pbo/api/rental_api.php"

    @property
    def id(self):
        return self.__id

    @property
    def kodeps(self):
        return self.__kodeps

    @kodeps.setter
    def kodeps(self, value):
        self.__kodeps = value

    @property
    def kdpelanggan(self):
        return self.__kdpelanggan

    @kdpelanggan.setter
    def kdpelanggan(self, value):
        self.__kdpelanggan = value

    @property
    def tipe_ps(self):
        return self.__tipe_ps

    @tipe_ps.setter
    def tipe_ps(self, value):
        self.__tipe_ps = value

    @property
    def mulai(self):
        return self.__mulai

    @mulai.setter
    def mulai(self, value):
        self.__mulai = value

    @property
    def selesai(self):
        return self.__selesai

    @selesai.setter
    def selesai(self, value):
        self.__selesai = value

    def getBykodeps(self, kodeps):
        url = self.__url + "?kodeps=" + kodeps
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        if data:
            item = data[0]
            self.__id = item["id"]
            self.__kodeps = item["kodeps"]
            self.__kdpelanggan = item["kdpelanggan"]
            self.__tipe_ps = item["tipe_ps"]
            self.__mulai = item["mulai"]
            self.__selesai = item["selesai"]
        return data

    def simpan(self):
        payload = {
            "kodeps": self.__kodeps,
            "kdpelanggan": self.__kdpelanggan,
            "tipe_ps": self.__tipe_ps,
            "mulai": self.__mulai,
            "selesai": self.__selesai
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.__url, json=payload, headers=headers)
        return response.text

    def updateBykodeps(self, kodeps):
        url = self.__url + "?kodeps=" + kodeps
        payload = {
            "kodeps": self.__kodeps,
            "kdpelanggan": self.__kdpelanggan,
            "tipe_ps": self.__tipe_ps,
            "mulai": self.__mulai,
            "selesai": self.__selesai
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, json=payload, headers=headers)
        return response.text

    def getAllData(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, headers=headers)
        return response.text

    def deleteBykodeps(self, kodeps):
        url = self.__url + "?kodeps=" + kodeps
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url, headers=headers)
        return response.text

    def getAllPelanggan(self):
        url = "http://localhost/pbo/api/pelanggan_api.php"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        return response.text

import requests
import json

class Pelanggan:

    def __init__(self):
        self.__id = None
        self.__kode = None
        self.__nama = None
        self.__jk = None
        self.__alamat = None
        self.__telepon = None
        self.__url = "http://localhost/pbo/api/pelanggan_api.php"
               
    @property
    def id(self):
        return self.__id

    @property
    def kode(self):
        return self.__kode

    @kode.setter
    def kode(self, value):
        self.__kode = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def telepon(self):
        return self.__telepon

    @telepon.setter
    def telepon(self, value):
        self.__telepon = value
        
    def getByKode(self, kode):
        url = self.__url + "?kode=" + kode
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item["id"]
            self.__kode = item["kode"]
            self.__nama = item["nama"]
            self.__jk = item["jk"]
            self.__alamat = item["alamat"]
            self.__telepon = item["telepon"]
        return data

    def simpan(self):
        payload = {
            "kode": self.__kode,
            "nama": self.__nama,
            "jk": self.__jk,
            "alamat": self.__alamat,
            "telepon": self.__telepon
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateByKode(self, kode):
        url = self.__url + "?kode=" + kode
        payload = {
            "kode": self.__kode,
            "nama": self.__nama,
            "jk": self.__jk,
            "alamat": self.__alamat,
            "telepon": self.__telepon
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, headers=headers)
        return response.text
    
    def deleteByKode(self, kode):
        url = self.__url + "?kode=" + kode
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url, headers=headers)
        return response.text

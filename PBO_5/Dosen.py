from db import DBConnection as mydb

class Dosen:

    def __init__(self):
        self.__id=None
        self.__nid=None
        self.__nama=None
        self.__jk=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def nid(self):
        return self.__nid

    @nid.setter
    def nid(self, value):
        self.__nid = value

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

    def simpan(self):
        self.conn = mydb()
        val = (self.__nid, self.__nama, self.__jk)
        sql="INSERT INTO dosen (nid, nama, jk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nid, self.__nama, self.__jk, id)
        sql="UPDATE dosen SET nid = %s, nama = %s, jk=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBynid(self, nid):
        self.conn = mydb()
        val = (self.__nama, self.__jk, nid)
        sql="UPDATE dosen SET nama = %s, jk=%s WHERE nid=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBynid(self, nid):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE nid='" + str(nid) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nid = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.conn.disconnect
        return self.result

    def getBynid(self, nid):
        a=str(nid)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE nid='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nid = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nid = ''
            self.__nama = ''
            self.__jk = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dosen"
        self.result = self.conn.findAll(sql)
        return self.result

# delete Data
A = Dosen()
B = A.getAllData()
print(B)
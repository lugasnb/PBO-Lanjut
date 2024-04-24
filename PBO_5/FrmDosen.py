import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Dosen import Dosen

class FormDosen:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='NID:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNID = Entry(mainFrame) 
        self.txtNID.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNID.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Jenis Kelamin:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select() # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)    
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('iddsn', 'nid', 'nama','jk')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('iddsn', text='ID')
        self.tree.column('iddsn', width="30")
        self.tree.heading('nid', text='NID')
        self.tree.column('nid', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNID.delete(0,END)
        self.txtNID.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data Dosen
        dsn = Dosen()
        result = dsn.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        nid = self.txtNID.get()
        dsn = Dosen()
        res = dsn.getBynid(nid)
        rec = dsn.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nid = self.txtNID.get()
        dsn = Dosen()
        res = dsn.getBynid(nid)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,dsn.nama)
        jk = dsn.jk
        if(jk=="P"):
            self.P.select()
        else:
            self.L.select()   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        nid = self.txtNID.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()
        
        dsn = Dosen()
        dsn.nid = nid
        dsn.nama = nama
        dsn.jk = jk
        if(self.ditemukan==True):
            res = dsn.updateBynid(nid)
            ket = 'Diperbarui'
        else:
            res = dsn.simpan()
            ket = 'Disimpan'
            
        rec = dsn.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nid = self.txtNID.get()
        dsn = Dosen()
        dsn.nid = nid
        if(self.ditemukan==True):
            res = dsn.deleteBynid(nid)
            rec = dsn.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormDosen(root, "Aplikasi Data Dosen")
    root.mainloop() 
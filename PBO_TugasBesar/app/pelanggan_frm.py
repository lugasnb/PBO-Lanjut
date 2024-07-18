import tkinter as tk
import json
from tkinter import Frame, Label, Entry, Button, ttk, VERTICAL, YES, BOTH, END, Tk, W, StringVar, messagebox
from pelanggan import *

class PelangganFrm:
    
    def __init__(self, parent, title):
        self.parent = parent       
        # self.parent.geometry("500x500")
        # self.parent.title(title)
        # self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bg='#333533')
        mainFrame.pack()
        
        # Label
        Label(mainFrame, text='PELANGGAN', font=("Montserrat", 14, "bold"), fg='#FFD100', bg='#333533').grid(row=0, column=0, columnspan=5, padx=5, pady=20)
        Label(mainFrame, text='Kode:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=1, column=0, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Nama:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=2, column=0, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Jenis Kelamin:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Alamat:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=1, column=2, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Telepon:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=2, column=2, sticky=W, padx=10, pady=5)
        
        # Textbox
        self.txtKode = Entry(mainFrame, font=("Montserrat", 9, "bold"), width=17) 
        self.txtKode.grid(row=1, column=1, padx=10, pady=5) 
        self.txtKode.bind("<Return>", self.onCari)
        
        self.txtNama = Entry(mainFrame, font=("Montserrat", 9, "bold"), width=17) 
        self.txtNama.grid(row=2, column=1, padx=10, pady=5) 
        
        # Combobox for Jenis Kelamin
        self.txtJK = ttk.Combobox(mainFrame, font=("Montserrat", 9, "bold"), width=14, values=['L', 'P'], state='readonly')
        # self.txtJK.current(0)
        self.txtJK.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        self.txtAlamat = Entry(mainFrame, font=("Montserrat", 9, "bold"), width=17)
        self.txtAlamat.grid(row=1, column=3, padx=10, pady=5)
        
        self.txtTelepon = Entry(mainFrame, font=("Montserrat", 9, "bold"), width=17)
        self.txtTelepon.grid(row=2, column=3, padx=10, pady=5)
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', font=("Montserrat", 9, "bold"), bg='#FFEE32', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=1, column=4, padx=10, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', font=("Montserrat", 9, "bold"), bg='#FFEE32', command=self.onClear, width=10)
        self.btnClear.grid(row=2, column=4, padx=10, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', font=("Montserrat", 9, "bold"), bg='#FFEE32', command=self.onDelete, width=10)
        self.btnHapus.grid(row=3, column=4, padx=10, pady=5)

        # Style untuk Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Montserrat", 9, "bold"), anchor="center")
        style.configure("Treeview", font=("Montserrat", 9), rowheight=25)

        # Define columns
        columns = ('id', 'kode', 'nama', 'jk', 'alamat', 'telepon')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # Define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30", anchor="center")
        self.tree.heading('kode', text='Kode')
        self.tree.column('kode', width="60", anchor="center")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="150", anchor="center")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="40", anchor="center")
        self.tree.heading('alamat', text='Alamat')
        self.tree.column('alamat', width="150", anchor="center")
        self.tree.heading('telepon', text='Telepon')
        self.tree.column('telepon', width="100", anchor="center")
        
        # set tree position
        self.tree.grid(row=4, column=0, columnspan=5, padx=10, pady=20, sticky='nsew')

    def onClear(self, event=None):
        self.txtKode.delete(0, END)
        self.txtKode.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")       
        self.txtAlamat.delete(0, END)
        self.txtAlamat.insert(END, "")
        self.txtTelepon.delete(0, END)
        self.txtTelepon.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.txtJK.current(0)
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        pelanggan = Pelanggan()
        result = pelanggan.getAllData()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["kode"], d["nama"], d["jk"], d["alamat"], d["telepon"]))
    
    def onCari(self, event=None):
        kode = self.txtKode.get()
        pelanggan = Pelanggan()
        a = pelanggan.getByKode(kode)
        if len(a) > 0:
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        
        
    def TampilkanData(self, event=None):
        kode = self.txtKode.get()
        pelanggan = Pelanggan()
        res = pelanggan.getByKode(kode)
        
        if res and isinstance(res, list) and len(res) > 0 and isinstance(res[0], dict):
            data = res[0]
            self.txtNama.delete(0, END)
            self.txtNama.insert(END, data['nama'])
            self.txtJK.set(data['jk'])
            self.txtAlamat.delete(0, END)
            self.txtAlamat.insert(END, data['alamat'])
            self.txtTelepon.delete(0, END)
            self.txtTelepon.insert(END, data['telepon'])   
            self.btnSimpan.config(text="Update")
        else:
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
                    
    def onSimpan(self, event=None):
        kode = self.txtKode.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()
        alamat = self.txtAlamat.get() 
        telepon = self.txtTelepon.get()
        
        pelanggan = Pelanggan()
        
        pelanggan.kode = kode
        pelanggan.nama = nama
        pelanggan.jk = jk
        pelanggan.alamat = alamat
        pelanggan.telepon = telepon
        
        if not self.ditemukan:
            res = pelanggan.simpan()
        else:
            res = pelanggan.updateByKode(kode)
        
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        messagebox.showinfo("showinfo", status + ', ' + msg)
        
        self.onClear()

    def onDelete(self, event=None):
        kode = self.txtKode.get()
        pelanggan = Pelanggan()
        pelanggan.kode = kode
        if self.ditemukan:
            res = pelanggan.deleteByKode(kode)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        messagebox.showinfo("showinfo", status + ', ' + msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = PelangganFrm(root, "Aplikasi Data Pelanggan")
    root.mainloop()

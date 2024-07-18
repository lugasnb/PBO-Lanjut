import tkinter as tk
import json
from tkinter import Frame, Label, Entry, Button, ttk, BOTH, END, W, messagebox
from datetime import datetime
from rental import *

class RentalFrm:

    def __init__(self, parent, title):
        self.parent = parent
        # self.parent.geometry("500x500")
        # self.parent.title(title)
        # self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)     
        self.ditemukan = None
        self.aturKomponen()
        self.loadPelanggan()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bg='#333533')
        mainFrame.pack()
        
        # Label
        Label(mainFrame, text='RENTAL PLAYSTATION', font=("Montserrat", 14, "bold"), fg='#FFD100', bg='#333533').grid(row=0, column=0, columnspan=5, padx=5, pady=20)
        Label(mainFrame, text='Kode PS:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=1, column=0, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Pelanggan:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=2, column=0, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Tipe PS:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Mulai:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=1, column=2, sticky=W, padx=10, pady=5)
        Label(mainFrame, text='Selesai:', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=2, column=2, sticky=W, padx=10, pady=5)
        
        # Textbox
        self.txtkodeps = Entry(mainFrame, font=("Montserrat", 9, "bold"), width=17) 
        self.txtkodeps.grid(row=1, column=1, padx=10, pady=5) 
        self.txtkodeps.bind("<Return>", self.onCari)
        
        # Combobox untuk Pelanggan
        self.cboPelanggan = ttk.Combobox(mainFrame, font=("Montserrat", 9, "bold"), width=14, state="readonly")
        self.cboPelanggan.grid(row=2, column=1, padx=10, pady=5)
        
        # Combobox untuk Tipe PS
        self.cboTipePs = ttk.Combobox(mainFrame, font=("Montserrat", 9, "bold"), width=14, state="readonly", values=["PlayStation 3", "PlayStation 4", "PlayStation 5"])
        self.cboTipePs.grid(row=3, column=1, padx=10, pady=5)
        
        # Entry
        self.txtMulai = Entry(mainFrame, font=("Montserrat", 9, "bold"), width=18)
        self.txtMulai.grid(row=1, column=3, padx=10, pady=5)
        self.txtSelesai = Entry(mainFrame, font=("Montserrat", 9, "bold"), width=18)
        self.txtSelesai.grid(row=2, column=3, padx=10, pady=5)
        
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
        columns = ('id', 'kodeps', 'kdpelanggan', 'tipe_ps', 'mulai', 'selesai', 'durasi', 'harga', 'total')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')

        # Define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width=30, anchor="center")
        self.tree.heading('kodeps', text='Kode PS')
        self.tree.column('kodeps', width=70, anchor="center")
        self.tree.heading('kdpelanggan', text='Pelanggan')
        self.tree.column('kdpelanggan', width=80, anchor="center")
        self.tree.heading('tipe_ps', text='Tipe PS')
        self.tree.column('tipe_ps', width=100, anchor="center")
        self.tree.heading('mulai', text='Mulai')
        self.tree.column('mulai', width=140, anchor="center")
        self.tree.heading('selesai', text='Selesai')
        self.tree.column('selesai', width=140, anchor="center")
        self.tree.heading('durasi', text='Durasi')
        self.tree.column('durasi', width=60, anchor="center")
        self.tree.heading('harga', text='Harga per Jam')
        self.tree.column('harga', width=100, anchor="center")
        self.tree.heading('total', text='Total')
        self.tree.column('total', width=100, anchor="center")
        
        # Set tree position
        self.tree.grid(row=4, column=0, columnspan=5, padx=10, pady=20, sticky='nsew')

        # Set waktu saat ini
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.txtMulai.insert(END, current_time)
        self.txtSelesai.insert(END, current_time)

    def loadPelanggan(self):
        url = "http://localhost/pbo/api/pelanggan_api.php"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        pelanggan_list = json.loads(response.text)
        kode_pelanggan = [pelanggan["kode"] for pelanggan in pelanggan_list]
        self.cboPelanggan['values'] = kode_pelanggan


    def onClear(self, event=None):
        self.txtkodeps.delete(0, END)
        self.cboPelanggan.set("")
        self.cboTipePs.set("")
        self.txtMulai.delete(0, END)
        self.txtMulai.insert(END, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.txtSelesai.delete(0, END)
        self.txtSelesai.insert(END, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.loadPelanggan()
        self.ditemukan = False
        
    def onReload(self, event=None):
        self.loadPelanggan()

        for item in self.tree.get_children():
            self.tree.delete(item)

        rental = Rental()
        result = rental.getAllData()
        parsed_data = json.loads(result)

        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["kodeps"], d["kdpelanggan"], d["tipe_ps"], d["mulai"], d["selesai"], d["durasi"], d["harga"], d["total"]))
    
    def onCari(self, event=None):
        kodeps = self.txtkodeps.get()
        rental = Rental()
        a = rental.getBykodeps(kodeps)
        if len(a) > 0:
            self.TampilkanData(a[0])
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        
    def TampilkanData(self, data):
        self.txtkodeps.delete(0, END)
        self.txtkodeps.insert(END, data['kodeps'])
        self.cboPelanggan.set(data['kdpelanggan'])
        self.cboTipePs.set(data['tipe_ps'])
        self.txtMulai.delete(0, END)
        self.txtMulai.insert(END, data['mulai'])
        self.txtSelesai.delete(0, END)
        self.txtSelesai.insert(END, data['selesai'])
        self.btnSimpan.config(text="Update")
                
    def onSimpan(self, event=None):
        kodeps = self.txtkodeps.get()
        kdpelanggan = self.cboPelanggan.get()
        tipe_ps = self.cboTipePs.get()
        mulai = self.txtMulai.get()
        selesai = self.txtSelesai.get()

        rental = Rental()
        rental.kodeps = kodeps
        rental.kdpelanggan = kdpelanggan
        rental.tipe_ps = tipe_ps
        rental.mulai = mulai
        rental.selesai = selesai

        if not self.ditemukan:
            res = rental.simpan()
        else:
            res = rental.updateBykodeps(kodeps)

        try:
            data = json.loads(res)
            status = data["status"]
            msg = data["message"]
            messagebox.showinfo("showinfo", f"{status}, {msg}")
            self.onClear()
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", "Error decoding server response.")
            print(f"Error decoding JSON: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
            print(f"Unexpected error: {str(e)}")


    def onDelete(self, event=None):
        kodeps = self.txtkodeps.get()
        rental = Rental()
        rental.kodeps = kodeps
        if self.ditemukan:
            res = rental.deleteBykodeps(kodeps)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            return

        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        messagebox.showinfo("showinfo", f"{status}, {msg}")
        self.onClear()
        
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("Data Rental PS")
#     RentalFrm(root, "Data Rental PS")
#     root.mainloop()

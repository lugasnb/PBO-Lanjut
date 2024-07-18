import tkinter as tk
from tkinter import ttk, messagebox
import barang
import customer

class BarangFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=600, height=300)
        
        tk.Label(self, text="Tabel Barang", font=('Aptos', 14, 'bold')).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        tk.Label(self, text="Kode Barang", font=('Aptos', 10)).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Nama Barang", font=('Aptos', 10)).grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self, text="Harga", font=('Aptos', 10)).grid(row=3, column=0, padx=10, pady=5)
        
        self.kode_barang_entry = tk.Entry(self)
        self.kode_barang_entry.grid(row=1, column=1, padx=10, pady=5)
        self.kode_barang_entry.bind("<Return>", self.on_enter_kode_barang)
        
        self.nama_barang_entry = tk.Entry(self)
        self.nama_barang_entry.grid(row=2, column=1, padx=10, pady=5)
        self.harga_barang_entry = tk.Entry(self)
        self.harga_barang_entry.grid(row=3, column=1, padx=10, pady=5)

        self.save_barang_button = tk.Button(self, text="Simpan", font=('Aptos', 10), bg="#F7C232", command=self.save_or_update_barang)
        self.save_barang_button.grid(row=1, column=2, pady=5)
        self.delete_barang_button = tk.Button(self, text="Hapus", font=('Aptos', 10), bg="#F7C232", command=self.delete_barang)
        self.delete_barang_button.grid(row=2, column=2, pady=5)
        self.clear_barang_button = tk.Button(self, text="Bersihkan", font=('Aptos', 10), bg="#F7C232", command=self.clear_barang_fields)
        self.clear_barang_button.grid(row=3, column=2, pady=5)
        
        self.barang_tree = ttk.Treeview(self, columns=("id_barang", "kode_barang", "nama_barang", "harga"), show="headings", height=10)
        self.barang_tree.heading("id_barang", text="ID")
        self.barang_tree.heading("kode_barang", text="Kode Barang")
        self.barang_tree.heading("nama_barang", text="Nama Barang")
        self.barang_tree.heading("harga", text="Harga")
        
        self.barang_tree.column("id_barang", width=50, anchor=tk.CENTER)
        self.barang_tree.column("kode_barang", width=100, anchor=tk.CENTER)
        self.barang_tree.column("nama_barang", width=200, anchor=tk.CENTER)
        self.barang_tree.column("harga", width=100, anchor=tk.CENTER)
        
        self.barang_tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W+tk.E)
        self.barang_tree.bind("<ButtonRelease-1>", self.on_barang_select)
        
        self.read_barang()

    def on_enter_kode_barang(self, event):
        kode_barang = self.kode_barang_entry.get()
        found = False
        for item in self.barang_tree.get_children():
            item_values = self.barang_tree.item(item, "values")
            if item_values[1] == kode_barang:
                self.barang_tree.selection_set(item)
                self.barang_tree.focus(item)
                found = True
                break
        if not found:
            messagebox.showinfo("Info", "Data tidak ditemukan")

    def read_barang(self):
        for row in self.barang_tree.get_children():
            self.barang_tree.delete(row)
        
        barang_list = barang.get_barang()
        for b in barang_list:
            self.barang_tree.insert("", "end", values=(b['id_barang'], b['kode_barang'], b['nama_barang'], b['harga']))

    def save_or_update_barang(self):
        selected_item = self.barang_tree.selection()
        kode_barang = self.kode_barang_entry.get()
        nama_barang = self.nama_barang_entry.get()
        harga = self.harga_barang_entry.get()
        if selected_item:
            barang_id = self.barang_tree.item(selected_item)['values'][0]
            response = barang.update_barang(barang_id, kode_barang, nama_barang, harga)
        else:
            response = barang.create_barang(kode_barang, nama_barang, harga)
        messagebox.showinfo("Info", response['status_message'])
        self.read_barang()

    def delete_barang(self):
        selected_item = self.barang_tree.selection()
        if selected_item:
            barang_id = self.barang_tree.item(selected_item)['values'][0]
            response = barang.delete_barang(barang_id)
            messagebox.showinfo("Info", response['status_message'])
            self.read_barang()

    def clear_barang_fields(self):
        self.kode_barang_entry.delete(0, tk.END)
        self.nama_barang_entry.delete(0, tk.END)
        self.harga_barang_entry.delete(0, tk.END)
        self.barang_tree.selection_remove(self.barang_tree.selection())

    def on_barang_select(self, event):
        selected_item = self.barang_tree.focus()
        if selected_item:
            item_values = self.barang_tree.item(selected_item, "values")
            self.kode_barang_entry.delete(0, tk.END)
            self.kode_barang_entry.insert(0, item_values[1])
            self.nama_barang_entry.delete(0, tk.END)
            self.nama_barang_entry.insert(0, item_values[2])
            self.harga_barang_entry.delete(0, tk.END)
            self.harga_barang_entry.insert(0, item_values[3])


class CustomerFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=600, height=300)
        
        tk.Label(self, text="Tabel Customer", font=('Aptos', 14, 'bold')).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        tk.Label(self, text="KTP", font=('Aptos', 10)).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Nama Customer", font=('Aptos', 10)).grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self, text="Jenis Kelamin", font=('Aptos', 10)).grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self, text="Kota", font=('Aptos', 10)).grid(row=4, column=0, padx=10, pady=5)
        
        self.ktp_customer_entry = tk.Entry(self)
        self.ktp_customer_entry.grid(row=1, column=1, padx=10, pady=5)
        self.ktp_customer_entry.bind("<Return>", self.on_enter_ktp_customer)
        
        self.nama_customer_entry = tk.Entry(self)
        self.nama_customer_entry.grid(row=2, column=1, padx=10, pady=5)
        self.jk_customer_combobox = ttk.Combobox(self, values=["L", "P"], state="readonly")
        self.jk_customer_combobox.grid(row=3, column=1, padx=10, pady=5)
        self.kota_customer_entry = tk.Entry(self)
        self.kota_customer_entry.grid(row=4, column=1, padx=10, pady=5)

        self.save_customer_button = tk.Button(self, text="Simpan", font=('Aptos', 10), bg="#F7C232", command=self.save_or_update_customer)
        self.save_customer_button.grid(row=1, column=2, pady=5)
        self.delete_customer_button = tk.Button(self, text="Hapus", font=('Aptos', 10), bg="#F7C232", command=self.delete_customer)
        self.delete_customer_button.grid(row=2, column=2, pady=5)
        self.clear_customer_button = tk.Button(self, text="Bersihkan", font=('Aptos', 10), bg="#F7C232", command=self.clear_customer_fields)
        self.clear_customer_button.grid(row=3, column=2, pady=5)
        
        self.customer_tree = ttk.Treeview(self, columns=("id_customer", "ktp", "nama_customer", "jk", "kota"), show="headings", height=10)
        self.customer_tree.heading("id_customer", text="ID")
        self.customer_tree.heading("ktp", text="KTP")
        self.customer_tree.heading("nama_customer", text="Nama Customer")
        self.customer_tree.heading("jk", text="Jenis Kelamin")
        self.customer_tree.heading("kota", text="Kota")
        
        self.customer_tree.column("id_customer", width=50, anchor=tk.CENTER)
        self.customer_tree.column("ktp", width=100, anchor=tk.CENTER)
        self.customer_tree.column("nama_customer", width=200, anchor=tk.CENTER)
        self.customer_tree.column("jk", width=50, anchor=tk.CENTER)
        self.customer_tree.column("kota", width=100, anchor=tk.CENTER)
        
        self.customer_tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W+tk.E)
        self.customer_tree.bind("<ButtonRelease-1>", self.on_customer_select)
        
        self.read_customer()

    def on_enter_ktp_customer(self, event):
        ktp = self.ktp_customer_entry.get()
        found = False
        for item in self.customer_tree.get_children():
            item_values = self.customer_tree.item(item, "values")
            if item_values[1] == ktp:
                self.customer_tree.selection_set(item)
                self.customer_tree.focus(item)
                found = True
                break
        if not found:
            messagebox.showinfo("Info", "Data tidak ditemukan")

    def read_customer(self):
        for row in self.customer_tree.get_children():
            self.customer_tree.delete(row)
        
        customer_list = customer.get_customer()
        for c in customer_list:
            self.customer_tree.insert("", "end", values=(c['id_customer'], c['ktp'], c['nama_customer'], c['jk'], c['kota']))

    def save_or_update_customer(self):
        selected_item = self.customer_tree.selection()
        ktp = self.ktp_customer_entry.get()
        nama_customer = self.nama_customer_entry.get()
        jk = self.jk_customer_combobox.get()
        kota = self.kota_customer_entry.get()
        if selected_item:
            customer_id = self.customer_tree.item(selected_item)['values'][0]
            response = customer.update_customer(customer_id, ktp, nama_customer, jk, kota)
        else:
            response = customer.create_customer(ktp, nama_customer, jk, kota)
        messagebox.showinfo("Info", response['status_message'])
        self.read_customer()

    def delete_customer(self):
        selected_item = self.customer_tree.selection()
        if selected_item:
            customer_id = self.customer_tree.item(selected_item)['values'][0]
            response = customer.delete_customer(customer_id)
            messagebox.showinfo("Info", response['status_message'])
            self.read_customer()

    def clear_customer_fields(self):
        self.ktp_customer_entry.delete(0, tk.END)
        self.nama_customer_entry.delete(0, tk.END)
        self.jk_customer_combobox.set("")
        self.kota_customer_entry.delete(0, tk.END)
        self.customer_tree.selection_remove(self.customer_tree.selection())

    def on_customer_select(self, event):
        selected_item = self.customer_tree.focus()
        if selected_item:
            item_values = self.customer_tree.item(selected_item, "values")
            self.ktp_customer_entry.delete(0, tk.END)
            self.ktp_customer_entry.insert(0, item_values[1])
            self.nama_customer_entry.delete(0, tk.END)
            self.nama_customer_entry.insert(0, item_values[2])
            self.jk_customer_combobox.set(item_values[3])
            self.kota_customer_entry.delete(0, tk.END)
            self.kota_customer_entry.insert(0, item_values[4])


class APP(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("APP")
        
        window_width = 820
        window_height = 450
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        
        self.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        
        self.left_frame = tk.Frame(self, width=500, bg="#F7C232")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.barang_button = tk.Button(self.left_frame, text="Barang", bg='#1D3752', fg='#FFFFFF', font=('Aptos', 12), command=self.show_barang_frame)
        self.barang_button.pack(pady=20, fill=tk.X,)
        
        self.customer_button = tk.Button(self.left_frame, text="Customer", bg='#1D3752', fg='#FFFFFF', font=('Aptos', 12), command=self.show_customer_frame)
        self.customer_button.pack(pady=0, fill=tk.X)
        
        self.barang_frame = BarangFrame(self.main_frame)
        self.customer_frame = CustomerFrame(self.main_frame)
        
    def show_barang_frame(self):
        self.customer_frame.pack_forget()
        self.barang_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_customer_frame(self):
        self.barang_frame.pack_forget()
        self.customer_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = APP()
    app.mainloop()

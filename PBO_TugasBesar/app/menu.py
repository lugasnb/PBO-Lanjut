# File: menu.py

import tkinter as tk
from tkinter import Frame, Button, Label, messagebox
from rental_frm import RentalFrm
from pelanggan_frm import PelangganFrm
from login import LoginFrm

class Menu:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("880x550")
        self.parent.title(title)
        self.signed_in = False
        self.aturKomponen()
        self.openInitialFrame()
        
    def aturKomponen(self):
        self.topFrame = Frame(self.parent, bg='#202020')
        self.topFrame.pack(side=tk.TOP, fill=tk.X)

        self.bottomFrame = Frame(self.parent, bg='#333533')
        self.bottomFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.LblTitle = Label(self.topFrame, text='MENGELOLA RENTAL PLAYSTATION', font=("Montserrat", 14, "bold"), fg='#FFD100', bg='#202020')
        self.LblTitle.pack(side=tk.LEFT, padx=10, pady=15)

        if self.signed_in:
            self.btnSignIn = Button(self.topFrame, text='Logout', font=("Montserrat", 9), bg='#FFD100', command=self.logout)
        else:
            self.btnSignIn = Button(self.topFrame, text='Sign in', font=("Montserrat", 9), bg='#FFD100', command=self.openLoginFrame)
        
        self.btnSignIn.pack(side=tk.RIGHT, padx=10, pady=15)
        
        self.btnTabelPelanggan = Button(self.topFrame, text='Pelanggan', font=("Montserrat", 9), bg='#FFD100', command=self.openPelangganFrame, state=tk.DISABLED)
        self.btnTabelPelanggan.pack(side=tk.RIGHT, padx=10, pady=15)
        
        self.btnTabelPlaystation = Button(self.topFrame, text='Rental/Sewa', font=("Montserrat", 9), bg='#FFD100', command=self.openRentalFrame, state=tk.DISABLED)
        self.btnTabelPlaystation.pack(side=tk.RIGHT, padx=10, pady=15)

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def openInitialFrame(self):
        self.clearFrame(self.bottomFrame)
        # Tambahkan tampilan atau frame awal lainnya di sini, jika diperlukan.

    def openRentalFrame(self):
        if self.signed_in:
            self.clearFrame(self.bottomFrame)
            RentalFrm(self.bottomFrame, "Rental PlayStation")
        else:
            messagebox.showinfo("Info", "Maaf, Anda harus masuk terlebih dahulu.")

    def openPelangganFrame(self):
        if self.signed_in:
            self.clearFrame(self.bottomFrame)
            PelangganFrm(self.bottomFrame, "Pelanggan")
        else:
            messagebox.showinfo("Info", "Maaf, Anda harus masuk terlebih dahulu.")

    def openLoginFrame(self):
        self.clearFrame(self.bottomFrame)
        self.loginFrame = LoginFrm(self.bottomFrame, "Sign in", self)

    def logout(self):
        self.clearFrame(self.bottomFrame)
        self.signed_in = False
        self.btnSignIn.config(text='Sign in', command=self.openLoginFrame)
        self.btnTabelPlaystation.config(state=tk.DISABLED)
        self.btnTabelPelanggan.config(state=tk.DISABLED)
        self.openLoginFrame()

    def setSignedIn(self, status):
        self.signed_in = status
        if status:
            self.btnSignIn.config(text='Logout', command=self.logout)
            self.btnTabelPlaystation.config(state=tk.NORMAL)
            self.btnTabelPelanggan.config(state=tk.NORMAL)
            self.openInitialFrame()  # Tampilkan frame awal setelah berhasil login
        else:
            self.btnSignIn.config(text='Sign in', command=self.openLoginFrame)
            self.btnTabelPlaystation.config(state=tk.DISABLED)
            self.btnTabelPelanggan.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Menu(root, "Menu")
    root.mainloop()

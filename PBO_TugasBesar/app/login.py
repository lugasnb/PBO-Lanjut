# File: login.py

import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
import requests

class LoginFrm:

    def __init__(self, parent, title, menu):
        self.parent = parent
        self.menu = menu       
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bg='#333533')
        mainFrame.pack()

        Label(mainFrame, text='LOGIN', font=("Montserrat", 14, "bold"), fg='#FFD100', bg='#333533').grid(row=0, column=0, columnspan=2, padx=5, pady=20)
        Label(mainFrame, text='Username', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        Label(mainFrame, text='Password', font=("Montserrat", 9, "bold"), fg='#D6D6D6', bg='#333533').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.txtUsername = Entry(mainFrame, font=("Montserrat", 9), width='20') 
        self.txtUsername.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=5)
        self.txtPassword = Entry(mainFrame, font=("Montserrat", 9, "bold"), show='*', width='20') 
        self.txtPassword.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.btnLogin = Button(mainFrame, text='Login', font=("Montserrat", 9, "bold"), bg='#FFEE32', width='17', command=self.login)
        self.btnLogin.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW, padx=10, pady=10)

    def login(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        url = 'http://localhost/pbo/api/login_api.php'
        payload = {'username': username, 'password': password}

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            print(data)

            if response.status_code == 200 and data['status'] == 'success':
                messagebox.showinfo('Berhasil', 'Selamat Datang, ' + username + '!')
                self.menu.setSignedIn(True)
            else:
                messagebox.showerror('Gagal', 'Username atau password salah.')
        except requests.exceptions.RequestException as e:
            messagebox.showerror('Error', 'Connection Server.')


if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = LoginFrm(root, "Login Form", None)
    root.mainloop()

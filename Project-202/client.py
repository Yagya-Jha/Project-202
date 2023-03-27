import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected to the Server")

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.configure(bg="lightblue")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        
        self.pls = Label(self.login,text = "Please login to continue",justify = CENTER,font = "Helvetica 14 bold",bg="lightblue")
        self.pls.place( relheight = 0.15,relx = 0.2,rely = 0.07)
        self.labelName = Label(self.login,text = "Name: ",font = "Helvetica 12",bg="lightblue")
        self.labelName.place(relheight = 0.2,relx = 0.1,rely = 0.2)
        self.entryName = Entry(self.login,font = "Helvetica 14",bg="white")
        self.entryName.place(relwidth = 0.4,relheight = 0.12,relx = 0.35,rely = 0.2)
        self.entryName.focus()

        self.bttn=Button(self.login, text="Join Room", font = "Helvetica 14 bold",bg="lightgreen", command=lambda: self.goAhead(self.entryName.get()))
        self.bttn.place(relx=0.4,rely=0.5)
        
        self.Window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.name=name
g=GUI()

# while True:
#     data = client.recv(1024)
#     if not data:
#         break
#     print('Q.   ', data.decode('utf-8'))
    
#     # Take input from user
#     message = input('>> ')
    
#     # Send message to server
#     client.send(message.encode('utf-8'))

# client.close()

import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

Host = '127.0.0.1'
Port = 8080

class Client:

    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg= tkinter.Tk()
        msg.withdraw()

        self.nama = simpledialog.askstring("Nama", "Pilih nama",parent=msg)

        self.gui_done = False
        self.running = True

        
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

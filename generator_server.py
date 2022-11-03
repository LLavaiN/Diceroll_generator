import socket
import pickle
from tkinter import *
from tkinter import ttk
import threading

def sock():
    global redata
    sock = socket.socket()
    sock.bind(("", 14900))
    sock.listen(10)
    while True:
        conn, addr = sock.accept()
        udata = ""
        while True:
            data = conn.recv(64)
            if data:
        # output received data
                udata = pickle.loads(data)
           #tmp.append(str(data.decode("utf-8")))
            else:
                # no more data -- quit the loop
                conn.close()
                break
        redata = udata
        
        
thr1 = threading.Thread(target=sock, daemon=True)
thr1.start()

root = Tk()
redata=[]
counter=0

scr = Scrollbar(root)
tbl = ttk.Treeview(root, yscrollcommand=scr.set)
scr.config(command=tbl.yview)

tbl['columns']=('username','dice','result')

tbl.column("#0", width=0,  stretch=NO)
tbl.column("username",anchor=CENTER)
tbl.column("dice",anchor=CENTER)
tbl.column("result",anchor=CENTER)

tbl.heading("#0",text="",anchor=CENTER)
tbl.heading("username",text="Пользователь",anchor=CENTER)
tbl.heading("dice",text="Значение дайса",anchor=CENTER)
tbl.heading("result",text="Результат",anchor=CENTER)
while True:
    if redata:
    
        tbl.insert(parent='',index='end',iid=counter,text='',
        values=(redata[0],redata[2],redata[3]))
        redata = []
        counter = counter+1

    tbl.pack(fill=BOTH, side=LEFT, expand=True)
    scr.pack(fill=Y, side=RIGHT)

        
    root.update()

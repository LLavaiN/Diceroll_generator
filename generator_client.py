import socket
import pickle
import random
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import threading

def maker(dice):
    global username
    global address #"127.0.0.1"
    global port    #14900
    
    res = random.randint(1,int(dice))
    if(res == 20 and dice == 20):
        res = str(res)+", успех!"
    elif(res == 1 and dice == 20 ):
        res = str(res)+", провал!"
    test["text"] = f"{res}"
    printer(dice, res, history)
    print(srv_flag)
    conn = socket.socket()
    conn.connect((address, int(port)))
    alldata = [username,counter,dice,res]
    data = pickle.dumps(alldata)
    conn.send(data)
    conn.close()

def printer(dice, res, window):
    global counter
    tmpnum = counter+1
    tbl.insert(parent='',index='end',iid=counter,text='',
values=(tmpnum,dice,res))
 
    counter = tmpnum

def forbut_d4():
    maker(4)

def forbut_d6():
    maker(6)

def forbut_d8():
    maker(8)

def forbut_d10():
    maker(10)

def forbut_d12():
    maker(12)

def forbut_d20():
    maker(20)
    
def forbut_d100():
    maker(100)

def forbut_clear():
    for i in tbl.get_children():
        tbl.delete(i)
    global counter
    counter = 0


def forbut_savename(event):
    global username
    global address
    global port
    username = name_entry.get()
    address = address_entry.get()
    port = port_entry.get()
    new.destroy()

counter = 0
username = ""
address=""
port = 0


results = [[],[],[]]

new = Tk()
new.bind('<Return>',forbut_savename)

savename = Button(new, text = "ОК")
savename.bind('<Button-1>',forbut_savename)
name_lb = Label(new,text="Введите имя")
address_lb = Label(new,text="Введите адрес сервера")
port_lb = Label(new,text="Введите порт")
name_entry = Entry(new)
address_entry = Entry(new)
port_entry = Entry(new)

name_lb.pack()
name_entry.pack()
address_lb.pack()
address_entry.pack()
port_lb.pack()
port_entry.pack()
savename.pack()


new.mainloop()

root = Tk()
root.title("Генератор")
root.geometry("250x200+300+300")
root.rowconfigure([0,1,2,3,4],weight=1)
root.columnconfigure([0,1,2],weight=1)

d_font = font.Font(size=15, slant="italic")

test = Label(root, text=username+", бросай кубик!")
d4 = Button(root, text="D4", bg="#29FF45", command=forbut_d4)
d6 = Button(root, text="D6", bg="#FF5283", command=forbut_d6)
d8 = Button(root, text="D8", bg="#52FCFF", command=forbut_d8)
d10 = Button(root, text="D10", bg="#F082FF", command=forbut_d10)
d12 = Button(root, text="D12", bg="yellow", command=forbut_d12)
d20 = Button(root, text="D20", bg="white", command=forbut_d20)
d100 = Button(root, text="D100", bg="orange", command=forbut_d100)
clear = Button(root, text="Очистить историю", command=forbut_clear)


test['font'] = d_font

test.grid(column=0, row=0,columnspan=3,sticky=W+E+N+S)
d20.grid(column=0, row=1, columnspan=3,sticky=W+E+N+S)
d4.grid(column=0, row=2,sticky=W+E+N+S)
d6.grid(column=1, row=2,sticky=W+E+N+S)
d8.grid(column=2, row=2,sticky=W+E+N+S)
d10.grid(column=0, row=3,sticky=W+E+N+S)
d12.grid(column=1, row=3,sticky=W+E+N+S)
d100.grid(column=2, row=3,sticky=W+E+N+S)
clear.grid(column=0, row=4, columnspan=3,sticky=W+E+N+S)


history = Toplevel(root)
history.title("История ("+username+")")
history.columnconfigure(0,weight=1)
history.rowconfigure(0,weight=1)


scr = Scrollbar(history)
tbl = ttk.Treeview(history, yscrollcommand=scr.set)
scr.config(command=tbl.yview)

tbl['columns']=('№','dice','result')


tbl.column("#0", width=0,  stretch=NO)
tbl.column("№",anchor=CENTER)
tbl.column("dice",anchor=CENTER)
tbl.column("result",anchor=CENTER)

tbl.heading("#0",text="",anchor=CENTER)
tbl.heading("№",text="№",anchor=CENTER)
tbl.heading("dice",text="Значение дайса",anchor=CENTER)
tbl.heading("result",text="Результат",anchor=CENTER)

tbl.pack(fill=BOTH, side=LEFT, expand=True)
scr.pack(fill=Y, side=RIGHT)
root.mainloop()

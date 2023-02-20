from tkinter import *
from tkinter import ttk     #theme ของ tk
from tkinter import messagebox
import datetime

GUI = Tk()      #เรียกหน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล')    #title หน้าจอ
GUI.geometry('500x380')         #ขนาดหน้าจอ

L1 = Label(GUI, text='โปรแกรมบันทึกความรู้', font=('Angsana New', 22), fg='purple')
L1.place(x=30, y=10)

now=datetime.datetime.now()

def Button1() :
    txt = 'ปี ค.ศ. : ' + str(now.year)
    messagebox.showinfo('ปีปัจจุบัน', txt)

fb1 = Frame(GUI)
fb1.place(x=30, y=50)
b1 = ttk.Button(fb1, text='ปี ค.ศ. ปัจจุบัน', command=Button1)
b1.pack(ipadx=20, ipady=15)

def Button2() :
    txt = 'ปี พ.ศ. : ' + str(now.year + 543)
    messagebox.showinfo('ปีปัจจุบัน', txt)

fb2 = Frame(GUI)
fb2.place(x=30, y=120)
b2 = ttk.Button(fb2, text='ปี พ.ศ. ปัจจุบัน', command=Button2)
b2.pack(ipadx=20, ipady=15)




GUI.mainloop()

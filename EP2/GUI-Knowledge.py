from tkinter import *
from tkinter import ttk     #theme ของ tk
from tkinter import messagebox

GUI = Tk()      #เรียกหน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล')    #title หน้าจอ
GUI.geometry('500x380')         #ขนาดหน้าจอ


L1 = Label(GUI, text='โปรแกรมบันทึกความรู้', font=('Angsana New', 22), fg='purple')
L1.place(x=20, y=100)
b1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท ?')
b1.pack(ipadx=20, ipady=20)       #อยู่ตรงกลาง ขยายแกน x 20 ขยายแกน Y 20

def Button2() :
    txt = 'ตอนนี้มีเงินในบัญชี 3 ล้านบาท'
    messagebox.showinfo('เงินในบัญชี', txt)

fb1 = Frame(GUI)        #กำหนด canvas
fb1.place(x=100, y=200)
b2 = ttk.Button(fb1, text='เงินมีอยู่กี่บาท ?', command=Button2)         #สร้างปุ่มใน canvas fb1
b2.pack(ipadx=20, ipady=20)


GUI.mainloop()

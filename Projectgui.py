from nntplib import GroupInfo
from tkinter import *
import tkinter.messagebox
from turtle import width
from setuptools import Command
from tkinter import ttk
import sqlite3
amount=["a"]
data = sqlite3.connect("food.db")
shhooo=["a"]
cursor= data.execute('SELECT * FROM food') 
for i in cursor:
    shhooo.append(i[0])
cursor= data.execute('SELECT * FROM food') 
for i in cursor:
    shhooo.append(i[1])
cursor= data.execute('SELECT * FROM food') 
for i in cursor:
    shhooo.append(i[2])
cursor= data.execute('SELECT * FROM food') 
for i in cursor:
    shhooo.append(i[3])


data = sqlite3.connect("project1.db")
c = data.cursor() 



GUI = Tk()
GUI.title("แซบนัว")
GUI.geometry("800x650")



t=ttk.Notebook(GUI)
tk3=Frame(t)
root=Frame(t)
t.add(tk3,text="  โต๊ะ  ")
t.add(root,text="  เมนู  ")
t.pack(fill=BOTH,expand=1)

id_1=["a"]
table_1="0"

sh=StringVar()
def second():
    
        
        def c3(e):
            global table_1                   #จองโต๊ะ ดึงข้อมูลจาก database
            gender = e.widget["text"]
            cursor= data.execute('SELECT id,name FROM bt  WHERE name like "A%"')
            for i in cursor:
                if gender == i[1]:
                    id_1[i[0]]["bg"]="#cc5b47"
                    a_1=str ( i[0] )
                    sh.set(gender)

            c=data.cursor()     
            u_1=("#cc5b47",a_1)
            data.execute('update bt set bg = ? where id = ?',u_1)
            data.commit()
            c.close()
        
            table_1=gender


        def c4(e):
            global table_1                   #ตลิ๊กขวายกเลิกโต๊ะ
            gender = e.widget["text"]
            cursor= data.execute('SELECT id,name FROM bt  WHERE name like "A%"')
            for i in cursor:
                if gender == i[1]:
                    id_1[i[0]]["bg"]="#71c853"
                    _a=str ( i[0] )

            c=data.cursor()
            _o=("#71c853",_a)
            data.execute('update bt set bg = ? where id = ?',_o)
            data.commit()
            c.close()
        


        def c5(e):                          #เซ็ทเลข
            gender = e.widget["text"]
            sh.set(gender)

        button_n= data.execute('SELECT * FROM bt')            #สร้างปุ้มกดโดยดึงข้อมูลจาก database
        for i in button_n:
            id_1.append(i[0])
            id_1[i[0]]=Button(tk3,text =i[2],bg=i[7],font=15)
            id_1[i[0]].place(x=i[5],y=i[6],width=i[3],height=i[4])
            id_1[i[0]].bind("<Button-1>", c3)
            id_1[i[0]].bind("<Button-3>", c4)
            id_1[i[0]].bind("<Enter>",  c5)

        x1=Entry(tk3,textvariable=sh).place(x=65,y=5,width=75,height=30)

second()



def aapp1(e):
    gender = e.widget["text"]
    label1.place(x=19000,y=70)
    myfood1.place(x=25000,y=5)
    myfood2.place(x=25000,y=5)
    myfood3.place(x=25000,y=5)
    myfood4.place(x=25000,y=5)
    myfood5.place(x=25000,y=5)
    myfood6.place(x=25000,y=5)
    myfood7.place(x=25000,y=5)

    myprice1.place(x=25000,y=5)
    myprice2.place(x=25000,y=5)
    myprice3.place(x=25000,y=5)
    myprice4.place(x=25000,y=5)
    myprice5.place(x=25000,y=5)
    myprice6.place(x=25000,y=5)
    myprice7.place(x=25000,y=5)
    myprice8.place(x=25000,y=5)
    myprice9.place(x=25000,y=5)
    myprice10.place(x=25000,y=5)
    myprice11.place(x=25000,y=5)
    myprice12.place(x=25000,y=5)
    myprice13.place(x=25000,y=5)

    btn1.place(x=25000,y=5)
    btn2 .place(x=25000,y=5)
    btn3 .place(x=25000,y=5)
    btn4 .place(x=25000,y=5)
    btn5 .place(x=25000,y=5)
    btn6 .place(x=25000,y=5)
    btn7 .place(x=25000,y=5)
    btn8 .place(x=25000,y=5)
    btn9 .place(x=25000,y=5)
    btn10 .place(x=25000,y=5)


    label1.place(x=35000,y=70)
    btn99.place(x=20000,y=300)
    btn98.place(x=30000,y=300)
    btn97.place(x=40000,y=300)
    btn96.place(x=50000,y=300)

    

    myfood8.place(x=25000,y=5)
    myfood9.place(x=25000,y=5) 
    myfood10.place(x=25000,y=5)
    myfood11.place(x=25000,y=5)
    myfood12.place(x=25000,y=5)
    myfood13.place(x=25000,y=5)
    myfood14.place(x=25000,y=5)

    myprice14.place(x=25000,y=5)
    myprice15.place(x=25000,y=5)
    myprice16.place(x=25000,y=5)
    myprice17.place(x=25000,y=5)
    myprice18.place(x=25000,y=5)

    myprice19.place(x=25000,y=5)
    myprice20.place(x=25000,y=5)
    myprice21.place(x=25000,y=5)
    myprice22.place(x=25000,y=5)
    myprice23.place(x=25000,y=5)
    myprice24.place(x=25000,y=5)
    myprice25.place(x=25000,y=5)

    myprice26.place(x=25000,y=5)

    btn11.place(x=25000,y=5)
    btn12.place(x=25000,y=5)
    btn13.place(x=25000,y=5)
    btn14.place(x=25000,y=5)
    btn15.place(x=25000,y=5)
    btn16.place(x=25000,y=5)
    btn17.place(x=25000,y=5)
    btn18.place(x=25000,y=5)
    btn19.place(x=25000,y=5)
    btn20.place(x=25000,y=5)

    btn21.place(x=25000,y=5)

    myfood15.place(x=25000,y=5)
    myfood16.place(x=25000,y=5)
    myfood17.place(x=25000,y=5)
    myfood18.place(x=25000,y=5)
    myfood19.place(x=25000,y=5)
    myfood20.place(x=25000,y=5)
    myfood21.place(x=25000,y=5)

    myprice27.place(x=25000,y=5)
    myprice28.place(x=25000,y=5)
    myprice29.place(x=25000,y=5)
    myprice30.place(x=25000,y=5)
    myprice31.place(x=25000,y=5)
    myprice32.place(x=25000,y=5)
    myprice33.place(x=25000,y=5)
    myprice34.place(x=25000,y=5)
    myprice35.place(x=25000,y=5)
    myprice36.place(x=25000,y=5)
    myprice37.place(x=25000,y=5)
    myprice38.place(x=25000,y=5)
    myprice39.place(x=25000,y=5)

    btn22.place(x=25000,y=5)
    btn23 .place(x=25000,y=5)
    btn24 .place(x=25000,y=5)
    btn25 .place(x=25000,y=5)
    btn26 .place(x=25000,y=5)
    btn27 .place(x=25000,y=5)
    btn28 .place(x=25000,y=5)
    btn29 .place(x=25000,y=5)
    btn30 .place(x=25000,y=5)
    btn31 .place(x=25000,y=5)
    btn32 .place(x=25000,y=5)

    myfood22.place(x=25000,y=5)
    myfood23.place(x=25000,y=5)
    myfood24.place(x=25000,y=5)
    myfood25.place(x=25000,y=5)
    myfood26.place(x=25000,y=5)
    myfood27.place(x=25000,y=5)
    myfood28.place(x=25000,y=5)

    myprice40.place(x=25000,y=5)
    myprice41.place(x=25000,y=5)
    myprice42.place(x=25000,y=5)
    myprice43.place(x=25000,y=5)
    myprice44.place(x=25000,y=5)
    myprice45.place(x=25000,y=5)
    myprice46.place(x=25000,y=5)
    myprice47.place(x=25000,y=5)
    myprice48.place(x=25000,y=5)
    myprice49.place(x=25000,y=5)
    myprice50.place(x=25000,y=5)
    myprice51.place(x=25000,y=5)
    myprice52.place(x=25000,y=5)

    btn33.place(x=25000,y=5)
    btn34 .place(x=25000,y=5)
    btn35 .place(x=25000,y=5)
    btn36 .place(x=25000,y=5)
    btn37 .place(x=25000,y=5)
    btn38 .place(x=25000,y=5)
    btn39 .place(x=25000,y=5)
    btn40 .place(x=25000,y=5)
    btn41 .place(x=25000,y=5)
    btn42 .place(x=25000,y=5)
    btn43 .place(x=25000,y=5)
    
    kaiyang.place(x=10000,y=100)
    kormoo.place(x=10000,y=200)
    lin.place(x=10000,y=300)
    suea.place(x=10000,y=400)
    puang.place(x=10000,y=500)

    kaeng.place(x=13000,y=100)
    nuea.place(x=13000,y=200)
    tom.place(x=13000,y=300)
    kom.place(x=10030,y=400)
    au.place(x=13000,y=500)

    thai.place(x=10030,y=100)
    lao.place(x=13000,y=200)
    taeng.place(x=13000,y=300)
    pu.place(x=13000,y=400)
    pa.place(x=13000,y=500) 

    moo.place(x=13000,y=100)
    kai.place(x=13000,y=200)
    mooyong.place(x=13000,y=300)
    mooyor.place(x=13000,y=400)
    jeen.place(x=13000,y=500)

    btn100.place(x=650,y=560)

    if gender=="ย่าง":
        myfood1.place(x=335,y=5)
        myfood2.place(x=230,y=120)
        myfood3.place(x=230,y=220)
        myfood4.place(x=230,y=320)
        myfood5.place(x=230,y=420)
        myfood6.place(x=230,y=520)
        myfood7.place(x=480,y=60)

        myprice1.place(x=490,y=120)
        myprice2.place(x=490,y=220)
        myprice3.place(x=490,y=320)
        myprice4.place(x=490,y=420)
        myprice5.place(x=490,y=520)
        myprice6.place(x=550,y=60)
        myprice7.place(x=560,y=120)
        myprice8.place(x=560,y=220)
        myprice9.place(x=560,y=320)
        myprice10.place(x=560,y=420)
        myprice11.place(x=560,y=520)
        myprice12.place(x=560,y=580)
        myprice13.place(x=490,y=580)

        btn1.place(x=410,y=120)
        btn2 .place(x=440,y=120)
        btn3 .place(x=410,y=220)
        btn4 .place(x=440,y=220)
        btn5 .place(x=410,y=320)
        btn6 .place(x=440,y=320)
        btn7 .place(x=410,y=420)
        btn8 .place(x=440,y=420)
        btn9 .place(x=410,y=520)
        btn10 .place(x=440,y=520)

        kaiyang.place(x=130,y=100)
        kormoo.place(x=130,y=200)
        lin.place(x=130,y=300)
        suea.place(x=130,y=400)
        puang.place(x=130,y=500)



        btn99.place(x=700,y=100)
        btn98.place(x=700,y=170)
        btn97.place(x=700,y=240)
        btn96.place(x=700,y=310)


    

    elif gender=="ต้ม":
        myfood8.place(x=335,y=5)
        myfood9.place(x=230,y=120)
        myfood10.place(x=230,y=220)
        myfood11.place(x=230,y=320)
        myfood12.place(x=230,y=420)
        myfood13.place(x=230,y=520)
        myfood14.place(x=480,y=60)

        myprice14.place(x=490,y=120)
        myprice15.place(x=490,y=220)
        myprice16.place(x=490,y=320)
        myprice17.place(x=490,y=420)
        myprice18.place(x=490,y=520)
        myprice19.place(x=550,y=60)
        myprice20.place(x=560,y=120)
        myprice21.place(x=560,y=220)
        myprice22.place(x=560,y=320)
        myprice23.place(x=560,y=420)
        myprice24.place(x=560,y=520)
        myprice25.place(x=560,y=580)
        myprice26.place(x=490,y=580) 
        myprice12.place(x=560,y=580)               

        btn11.place(x=410,y=120)
        btn12 .place(x=440,y=120)
        btn13 .place(x=410,y=220)
        btn14 .place(x=440,y=220)
        btn15 .place(x=410,y=320)
        btn16 .place(x=440,y=320)
        btn17 .place(x=410,y=420)
        btn18 .place(x=440,y=420)
        btn19 .place(x=410,y=520)
        btn20 .place(x=440,y=520)

        kaeng.place(x=130,y=100)
        nuea.place(x=130,y=200)
        tom.place(x=130,y=300)
        kom.place(x=130,y=400)
        au.place(x=130,y=500)


        btn99.place(x=700,y=100)
        btn98.place(x=700,y=170)
        btn97.place(x=700,y=240)
        btn96.place(x=700,y=310)
       
    elif gender=="ส้มตำ":
        myfood15.place(x=335,y=5)
        myfood16.place(x=230,y=120)
        myfood17.place(x=230,y=220)
        myfood18.place(x=230,y=320)
        myfood19.place(x=230,y=420)
        myfood20.place(x=230,y=520)
        myfood21.place(x=480,y=60)

        myprice27.place(x=490,y=120)
        myprice28.place(x=490,y=220)
        myprice29.place(x=490,y=320)
        myprice30.place(x=490,y=420)
        myprice31.place(x=490,y=520)
        myprice32.place(x=550,y=60)
        myprice33.place(x=560,y=120)
        myprice34.place(x=560,y=220)
        myprice35.place(x=560,y=320)
        myprice36.place(x=560,y=420)
        myprice37.place(x=560,y=520)
        myprice38.place(x=560,y=580)
        myprice39.place(x=490,y=580) 
        myprice12.place(x=560,y=580) 

        btn22.place(x=410,y=120)
        btn23 .place(x=440,y=120)
        btn24 .place(x=410,y=220)
        btn25 .place(x=440,y=220)
        btn26 .place(x=410,y=320)
        btn27 .place(x=440,y=320)
        btn28 .place(x=410,y=420)
        btn29 .place(x=440,y=420)
        btn30 .place(x=410,y=520)
        btn31 .place(x=440,y=520)

        thai.place(x=130,y=100)
        lao.place(x=130,y=200)
        taeng.place(x=130,y=300)
        pu.place(x=130,y=400)
        pa.place(x=130,y=500)   

        btn99.place(x=700,y=100)
        btn98.place(x=700,y=170)
        btn97.place(x=700,y=240)
        btn96.place(x=700,y=310)     
   
    elif gender=="ของกินเล่น":
        myfood22.place(x=335,y=5)
        myfood23.place(x=230,y=120)
        myfood24.place(x=230,y=220)
        myfood25.place(x=230,y=320)
        myfood26.place(x=230,y=420)
        myfood27.place(x=230,y=520)
        myfood28.place(x=480,y=60)

        myprice40.place(x=490,y=120)
        myprice41.place(x=490,y=220)
        myprice42.place(x=490,y=320)
        myprice43.place(x=490,y=420)
        myprice44.place(x=490,y=520)
        myprice45.place(x=550,y=60)
        myprice46.place(x=560,y=120)
        myprice47.place(x=560,y=220)
        myprice48.place(x=560,y=320)
        myprice49.place(x=560,y=420)
        myprice50.place(x=560,y=520)
        myprice12.place(x=560,y=580)
        myprice52.place(x=490,y=580) 

        btn33.place(x=410,y=120)
        btn34 .place(x=440,y=120)
        btn35 .place(x=410,y=220)
        btn36 .place(x=440,y=220)
        btn37 .place(x=410,y=320)
        btn38 .place(x=440,y=320)
        btn39 .place(x=410,y=420)
        btn40 .place(x=440,y=420)
        btn41 .place(x=410,y=520)
        btn42 .place(x=440,y=520)

        moo.place(x=130,y=100)
        kai.place(x=130,y=200)
        mooyong.place(x=130,y=300)
        mooyor.place(x=130,y=400)
        jeen.place(x=130,y=500)

        btn99.place(x=700,y=100)
        btn98.place(x=700,y=170)
        btn97.place(x=700,y=240)
        btn96.place(x=700,y=310)


def fffpay():
    aa=""
    bb=0
    if amount1.get() != 0:
        txtarea.insert(END,f" {shhooo[1]}\t\t\t{amount1.get()}\t\t\t{amount1.get()*120}\n")
        aa+=shhooo[1]+ f"({amount1.get()}"+"\n"
        bb+=amount1.get()*120

    if amount2.get() != 0:
        txtarea.insert(END,f" {shhooo[2]}\t\t\t{amount2.get()}\t\t\t{amount2.get()*70} \n")
        aa+=shhooo[2]+ f"({amount2.get()}"+"\n"
        bb+=amount1.get()*70

    if amount3.get() != 0:
        txtarea.insert(END,f" {shhooo[3]}\t\t\t{amount3.get()}\t\t\t{amount3.get()*60} \n")
        aa+=shhooo[3]+ f"({amount3.get()}"+"\n"
        bb+=amount1.get()*60

    if amount4.get() != 0:
        txtarea.insert(END,f" {shhooo[4]}\t\t\t{amount4.get()}\t\t\t{amount4.get()*70} \n")
        aa+=shhooo[4]+ f"({amount4.get()}"+"\n"
        bb+=amount1.get()*70

    if amount5.get() != 0:
        txtarea.insert(END,f" {shhooo[5]}\t\t\t{amount5.get()}\t\t\t{amount5.get()*70} \n")
        aa+=shhooo[5]+ f"({amount5.get()}"+"\n"
        bb+=amount1.get()*70

    if amount12.get() != 0:
        txtarea.insert(END,f" {shhooo[6]}\t\t\t{amount12.get()}\t\t\t{amount12.get()*70} \n")
        aa+=shhooo[6]+ f"({amount12.get()}"+"\n"
        bb+=amount1.get()*70

    if amount13.get() != 0:
        txtarea.insert(END,f" {shhooo[7]}\t\t\t{amount13.get()}\t\t\t{amount13.get()*80} \n")
        aa+=shhooo[7]+ f"({amount13.get()}"+"\n"
        bb+=amount1.get()*80

    if amount14.get() != 0:
        txtarea.insert(END,f" {shhooo[8]}\t\t\t{amount14.get()}\t\t\t{amount14.get()*75} \n")
        aa+=shhooo[8]+ f"({amount14.get()}"+"\n"
        bb+=amount1.get()*75

    if amount15.get() != 0:
        txtarea.insert(END,f" {shhooo[9]}\t\t\t{amount15.get()}\t\t\t{amount15.get()*75} \n")
        aa+=shhooo[9]+ f"({amount15.get()}"+"\n"
        bb+=amount1.get()*75

    if amount16.get() != 0:
        txtarea.insert(END,f" {shhooo[10]}\t\t\t{amount16.get()}\t\t\t{amount16.get()*75} \n")
        aa+=shhooo[10]+ f"({amount16.get()}"+"\n"
        bb+=amount1.get()*75

    if amount23.get() != 0:
        txtarea.insert(END,f" {shhooo[11]}\t\t\t{amount23.get()}\t\t\t{amount23.get()*40} \n")
        aa+=shhooo[11]+ f"({amount23.get()}"+"\n"
        bb+=amount1.get()*40

    if amount24.get() != 0:
        txtarea.insert(END,f" {shhooo[12]}\t\t\t{amount24.get()}\t\t\t{amount24.get()*40} \n")
        aa+=shhooo[12]+ f"({amount24.get()}"+"\n"
        bb+=amount1.get()*40

    if amount25.get() != 0:
        txtarea.insert(END,f" {shhooo[13]}\t\t\t{amount25.get()}\t\t\t{amount25.get()*40} \n")
        aa+=shhooo[13]+ f"({amount25.get()}"+"\n"
        bb+=amount1.get()*40

    if amount26.get() != 0:
        txtarea.insert(END,f" {shhooo[14]}\t\t\t{amount26.get()}\t\t\t{amount26.get()*45} \n")
        aa+=shhooo[14]+ f"({amount26.get()}"+"\n"
        bb+=amount1.get()*45

    if amount27.get() != 0:
        txtarea.insert(END,f" {shhooo[15]}\t\t\t{amount27.get()}\t\t\t{amount27.get()*50} \n")
        aa+=shhooo[15]+ f"({amount27.get()}"+"\n"
        bb+=amount1.get()*50

    if amount34.get() != 0:
        txtarea.insert(END,f" {shhooo[16]}\t\t\t{amount34.get()}\t\t\t{amount34.get()*10} \n")
        aa+=shhooo[16]+ f"({amount34.get()}"+"\n"
        bb+=amount1.get()*10

    if amount35.get() != 0:
        txtarea.insert(END,f" {shhooo[17]}\t\t\t{amount35.get()}\t\t\t{amount35.get()*10} \n")
        aa+=shhooo[17]+ f"({amount35.get()}"+"\n"
        bb+=amount1.get()*10

    if amount36.get() != 0:
        txtarea.insert(END,f" {shhooo[18]}\t\t\t{amount36.get()}\t\t\t{amount36.get()*10} \n")
        aa+=shhooo[18]+ f"({amount36.get()}"+"\n"
        bb+=amount1.get()*10

    if amount37.get() != 0:
        txtarea.insert(END,f" {shhooo[19]}\t\t\t{amount37.get()}\t\t\t{amount37.get()*20} \n")
        aa+=shhooo[19]+ f"({amount37.get()}"+"\n"
        bb+=amount1.get()*20

    if amount38.get() != 0:
        txtarea.insert(END,f" {shhooo[20]}\t\t\t{amount38.get()}\t\t\t{amount38.get()*10} \n")
        aa+=shhooo[20]+ f"({amount38.get()}"+"\n"
        bb+=amount1.get()*10
    txtarea.insert(END,f"รวม \t\t\t\t\t\t {amount11.get()} \n\n\n")
    c=data.cursor()
    c.execute(f"""INSERT INTO ab (_Table,_list,_price) VALUES ("{sh.get()}","{aa}","{amount11.get()}") """)
    data.commit()
    c.close()
    txtarea.insert(END,"พร้อมเพย์ 0930878790 \t\t\t\t\t\t  \n")

    

        

def pay():        #ที่อยู่บิล header บิล
    billarea.place(x=0,y=0,width=740,height=650)
    txtarea.delete(1.0,END)
    txtarea.insert(END,f"\nName : ")
    fffpay()


    btn_1111.place(x=740,y=0,width=50,height=50)
def pay_1():    
    billarea.place(x=10000,y=0,width=740,height=650)
    btn_1111.place(x=74000,y=0,width=50,height=50)
    




#--------------------------------------------------------------------------
photo99 = PhotoImage(file="2 (1).png")
Label(root, image=photo99).pack()

photo0 = PhotoImage(file="images.png")
logo = Label(root, image=photo0).pack()


photo1 = PhotoImage(file = "ไก่ย่าง.png")
kaiyang = Label(root,image=photo1)

photo2 = PhotoImage(file = "คอหมุย่าง.png")
kormoo = Label(root,image=photo2)

photo3 = PhotoImage(file = "ลิ้นย่าง.png")
lin = Label(root,image=photo3)

photo4 = PhotoImage(file = "เสือร้องไห้.png")
suea = Label(root,image=photo4)

photo5 = PhotoImage(file = "พวงนมย่าง.png")
puang = Label(root,image=photo5)

photo6 = PhotoImage(file = "แกงอ่อมหมู.png")
kaeng = Label(root,image=photo6)

photo7 = PhotoImage(file = "แกงอ่อมเนิ้อ.png")
nuea = Label(root,image=photo7)

photo8 = PhotoImage(file = "ต้มแซบกระดูกหมู.png")
tom = Label(root,image=photo8)

photo9 = PhotoImage(file = "ต้มขม.png")
kom = Label(root,image=photo9)

photo10 = PhotoImage(file = "อุเพี้ย.png")
au = Label(root,image=photo10)

photo11 = PhotoImage(file = "ตำลาว.png")
thai = Label(root,image=photo11)

photo12 = PhotoImage(file = "ตำไทย.png")
lao = Label(root,image=photo12)

photo13 = PhotoImage(file = "ตำแตง.png")
taeng = Label(root,image=photo13)

photo14 = PhotoImage(file = "ตำปูปลาร้า.png")
pu = Label(root,image=photo14)

photo15 = PhotoImage(file = "ตำป่า.png")
pa = Label(root,image=photo15)

photo16 = PhotoImage(file = "แคปหมู.png")
moo = Label(root,image=photo16)

photo17 = PhotoImage(file = "แคปไก่.png")
kai = Label(root,image=photo17)

photo18 = PhotoImage(file = "หมูหยอง.png")
mooyong = Label(root,image=photo18)

photo19 = PhotoImage(file = "หมูยอ.png")
mooyor = Label(root,image=photo19)

photo20 = PhotoImage(file = "ขนมจีน.png")
jeen = Label(root,image=photo20)







btn100 = Button(root,text="สั่งและจ่ายเงิน",bg="light green",fg="salmon",font=("thsarabunpsk 20"),command=pay)


label1 = Label(root, text="แซบนัว",bg="#7B68EE",font=("thsarabunpsk 36"), fg="red")
label1.place(x=350,y=70)
btn99 = Button(root,text="ย่าง",bg="orange",font=("thsarabunpsk 20"))
btn99.bind("<Button-1>", aapp1)
btn99.place(x=200,y=300)
btn98 = Button(root,text="ต้ม",bg="orange",font=("thsarabunpsk 20"))
btn98.bind("<Button-1>", aapp1)
btn98.place(x=300,y=300)
btn97 = Button(root,text="ส้มตำ",bg="orange",font=("thsarabunpsk 20"))
btn97.bind("<Button-1>", aapp1)
btn97.place(x=400,y=300)
btn96 = Button(root,text="ของกินเล่น",bg="orange",font=("thsarabunpsk 20"))
btn96.bind("<Button-1>", aapp1)
btn96.place(x=500,y=300)


btn91 = Button(root,text="ย่าง",bg="orange",font=("thsarabunpsk 20"))
btn92 = Button(root,text="ต้ม",bg="orange",font=("thsarabunpsk 20"))
btn93 = Button(root,text="ส้มตำ",bg="orange",font=("thsarabunpsk 20"))
btn94 = Button(root,text="ของกินเล่น",bg="orange",font=("thsarabunpsk 20"))





#---------------------------------------------------------------------------

amount1_cnt = 0
amount2_cnt = 0
amount3_cnt = 0
amount4_cnt = 0
amount5_cnt = 0
amount6_cnt = 0
amount7_cnt = 0
amount8_cnt = 0
amount9_cnt = 0
amount10_cnt = 0
amount11_cnt = 0



def add1():
    global amount1_cnt
    amount1_cnt +=1
    amount1.set(amount1_cnt)
    global amount6_cnt
    amount6_cnt +=120
    amount6.set(amount6_cnt)
    global amount11_cnt
    amount11_cnt +=120
    amount11.set(amount11_cnt)


    

def minus1():
    global amount1_cnt
    amount1_cnt -=1
    if amount1_cnt<=-1:
        amount1_cnt=0
    else: 
        amount1.set(amount1_cnt)
    global amount6_cnt
    amount6_cnt -=120
    if amount6_cnt<=-120:
        amount6_cnt=0
    else: 
        amount6.set(amount6_cnt)
    global amount11_cnt
    amount11_cnt -=120
    if amount11_cnt<=-25:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)


def add2():
    global amount2_cnt
    amount2_cnt +=1
    amount2.set(amount2_cnt)
    global amount7_cnt
    amount7_cnt +=70
    amount7.set(amount7_cnt)
    global amount11_cnt
    amount11_cnt +=70
    amount11.set(amount11_cnt)



def minus2():
    global amount2_cnt
    amount2_cnt -=1
    if amount2_cnt<=-1:
        amount2_cnt=0
    else: 
        amount2.set(amount2_cnt)
    global amount7_cnt
    amount7_cnt -=70
    if amount7_cnt<=-70:
        amount7_cnt=0
    else: 
        amount7.set(amount7_cnt)
    global amount11_cnt
    amount11_cnt -=70
    if amount11_cnt<=-70:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add3():
    global amount3_cnt
    amount3_cnt +=1
    amount3.set(amount3_cnt)
    global amount8_cnt
    amount8_cnt +=60
    amount8.set(amount8_cnt)
    global amount11_cnt
    amount11_cnt +=60
    amount11.set(amount11_cnt)

def minus3():
    global amount3_cnt
    amount3_cnt -=1
    if amount3_cnt<=-1:
        amount3_cnt=0
    else: 
        amount3.set(amount3_cnt)
    global amount8_cnt
    amount8_cnt -=60
    if amount8_cnt<=-60:
        amount8_cnt=0
    else: 
        amount8.set(amount8_cnt)
    global amount11_cnt
    amount11_cnt -=60
    if amount11_cnt<=-60:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add4():
    global amount4_cnt
    amount4_cnt +=1
    amount4.set(amount4_cnt)
    global amount9_cnt
    amount9_cnt +=70
    amount9.set(amount9_cnt)
    global amount11_cnt
    amount11_cnt +=70
    amount11.set(amount11_cnt)

def minus4():
    global amount4_cnt
    amount4_cnt -=1
    if amount4_cnt<=-1:
        amount4_cnt=0
    else: 
        amount4.set(amount4_cnt)
    global amount9_cnt
    amount9_cnt -=70
    if amount9_cnt<=-70:
        amount9_cnt=0
    else: 
        amount9.set(amount9_cnt)
    global amount11_cnt
    amount11_cnt -=70
    if amount11_cnt<=-70:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add5():
    global amount5_cnt
    amount5_cnt +=1
    amount5.set(amount5_cnt)
    global amount10_cnt
    amount10_cnt +=70
    amount10.set(amount10_cnt)
    global amount11_cnt
    amount11_cnt +=70
    amount11.set(amount11_cnt)

def minus5():
    global amount5_cnt
    amount5_cnt -=1
    if amount5_cnt<=-1:
        amount5_cnt=0
    else: 
        amount5.set(amount5_cnt)
    global amount10_cnt
    amount10_cnt -=70
    if amount10_cnt<=-70:
        amount10_cnt=0
    else: 
        amount10.set(amount10_cnt)
    global amount11_cnt
    amount11_cnt -=70
    if amount11_cnt<=-70:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def addproduct():
    tkinter.messagebox.showinfo("","หยิบสินค้าใส่ตะกร้าแล้ว")
    data.commit()



amount1 = IntVar()
amount2 = IntVar()
amount3 = IntVar()
amount4 = IntVar()
amount5 = IntVar()
amount6 = IntVar()
amount7 = IntVar()
amount8 = IntVar()
amount9 = IntVar()
amount10 = IntVar()
amount11 = IntVar()


myfood1 = Label(root,text="ย่าง",fg="black",bg="lawngreen",font=("thsarabunpsk 40"))
myfood2 = Label(root,text="ไก่ย่าง",fg="black",bg="salmon",font=("thsarabunpsk 20"),)
myfood3 = Label(root,text="คอหมูย่าง",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood4 = Label(root,text="ลิ้นย่าง",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood5 = Label(root,text="เสือร้องไห้",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood6 = Label(root,text="พวงนมย่าง",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood7 = Label(root,text="จำนวน",fg="black",bg="salmon",font=("thsarabunpsk 20"))

myprice1 = Label(root,textvariable=amount1,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice2 = Label(root,textvariable=amount2,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice3 = Label(root,textvariable=amount3,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice4 = Label(root,textvariable=amount4,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice5 = Label(root,textvariable=amount5,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))

myprice6 = Label(root,text="ราคา",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myprice7 = Label(root,textvariable=amount6,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice8 = Label(root,textvariable=amount7,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice9 = Label(root,textvariable=amount8,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice10 = Label(root,textvariable=amount9,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice11 = Label(root,textvariable=amount10,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice12 = Label(root,textvariable=amount11,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))

myprice13 = Label(root,text="รวม",fg="black",bg="lightgreen",font=("thsarabunpsk 15"))

btn1 = Button(root,text="-",bg="salmon",command=minus1,)
btn2 = Button(root,text="+",bg="light green",command=add1)
btn3 = Button(root,text="-",bg="salmon",command=minus2)
btn4 = Button(root,text="+",bg="light green",command=add2)
btn5 = Button(root,text="-",bg="salmon",command=minus3)
btn6 = Button(root,text="+",bg="light green",command=add3)
btn7 = Button(root,text="-",bg="salmon",command=minus4)
btn8 = Button(root,text="+",bg="light green",command=add4)
btn9 = Button(root,text="-",bg="salmon",command=minus5)
btn10 = Button(root,text="+",bg="light green",command=add5)



#--------------------------------------------------------------------------------------------------------

amount12_cnt = 0
amount13_cnt = 0
amount14_cnt = 0
amount15_cnt = 0
amount16_cnt = 0
amount17_cnt = 0
amount18_cnt = 0
amount19_cnt = 0
amount20_cnt = 0
amount21_cnt = 0
amount22_cnt = 0


def add1():
    global amount12_cnt
    amount12_cnt +=1
    amount12.set(amount12_cnt)
    global amount17_cnt
    amount17_cnt +=70
    amount17.set(amount17_cnt)
    global amount11_cnt
    amount11_cnt +=70
    amount11.set(amount11_cnt)
    

def minus1():
    global amount12_cnt
    amount12_cnt -=1
    if amount12_cnt<=-1:
        amount12_cnt=0
    else: 
        amount12.set(amount12_cnt)
    global amount17_cnt
    amount17_cnt -=70
    if amount17_cnt<=-70:
        amount17_cnt=0
    else: 
        amount17.set(amount17_cnt)
    global amount11_cnt
    amount11_cnt -=70
    if amount11_cnt<=-70:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add2():
    global amount13_cnt
    amount13_cnt +=1
    amount13.set(amount13_cnt)
    global amount18_cnt
    amount18_cnt +=80
    amount18.set(amount18_cnt)
    global amount11_cnt
    amount11_cnt +=80
    amount11.set(amount11_cnt)

def minus2():
    global amount13_cnt
    amount13_cnt -=1
    if amount13_cnt<=-1:
        amount13_cnt=0
    else: 
        amount13.set(amount13_cnt)
    global amount18_cnt
    amount18_cnt -=80
    if amount18_cnt<=-80:
        amount18_cnt=0
    else: 
        amount18.set(amount18_cnt)
    global amount11_cnt
    amount11_cnt -=80
    if amount11_cnt<=-80:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add3():
    global amount14_cnt
    amount14_cnt +=1
    amount14.set(amount14_cnt)
    global amount19_cnt
    amount19_cnt +=75
    amount19.set(amount19_cnt)
    global amount11_cnt
    amount11_cnt +=75
    amount11.set(amount11_cnt)

def minus3():
    global amount14_cnt
    amount14_cnt -=1
    if amount14_cnt<=-1:
        amount14_cnt=0
    else: 
        amount14.set(amount14_cnt)
    global amount19_cnt
    amount19_cnt -=75
    if amount19_cnt<=-75:
        amount19_cnt=0
    else: 
        amount19.set(amount19_cnt)
    global amount11_cnt
    amount11_cnt -=75
    if amount11_cnt<=-75:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add4():
    global amount15_cnt
    amount15_cnt +=1
    amount15.set(amount15_cnt)
    global amount20_cnt
    amount20_cnt +=75
    amount20.set(amount20_cnt)
    global amount11_cnt
    amount11_cnt +=75
    amount11.set(amount11_cnt)

def minus4():
    global amount15_cnt
    amount15_cnt -=1
    if amount15_cnt<=-1:
        amount15_cnt=0
    else: 
        amount15.set(amount15_cnt)
    global amount20_cnt
    amount20_cnt -=75
    if amount20_cnt<=-75:
        amount20_cnt=0
    else: 
        amount20.set(amount20_cnt)
    global amount11_cnt
    amount11_cnt -=75
    if amount11_cnt<=-75:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add5():
    global amount16_cnt
    amount16_cnt +=1
    amount16.set(amount16_cnt)
    global amount21_cnt
    amount21_cnt +=75
    amount21.set(amount21_cnt)
    global amount11_cnt
    amount11_cnt +=75
    amount11.set(amount11_cnt)

def minus5():
    global amount16_cnt
    amount16_cnt -=1
    if amount16_cnt<=-1:
        amount16_cnt=0
    else: 
        amount16.set(amount16_cnt)
    global amount21_cnt
    amount21_cnt -=75
    if amount21_cnt<=-75:
        amount21_cnt=0
    else: 
        amount21.set(amount21_cnt)
    global amount11_cnt
    amount11_cnt -=75
    if amount11_cnt<=-75:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def addproduct():
    tkinter.messagebox.showinfo("","หยิบสินค้าใส่ตะกร้าแล้ว")



amount12 = IntVar()
amount13 = IntVar()
amount14 = IntVar()
amount15 = IntVar()
amount16 = IntVar()
amount17 = IntVar()
amount18 = IntVar()
amount19 = IntVar()
amount20 = IntVar()
amount21 = IntVar()
amount22 = IntVar()


myfood8 = Label(root,text="ต้ม",fg="black",bg="lawngreen",font=("thsarabunpsk 40"))
myfood9 = Label(root,text="แกงอ่อมหมู",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood10 = Label(root,text="แกงอ่อมเนื้อ",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood11 = Label(root,text="ต้มกระดูกแซ่บ",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood12 = Label(root,text="ต้มขม",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood13 = Label(root,text="อุเพี้ย",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood14 = Label(root,text="จำนวน",fg="black",bg="salmon",font=("thsarabunpsk 20"))

myprice14 = Label(root,textvariable=amount12,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice15= Label(root,textvariable=amount13,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice16 = Label(root,textvariable=amount14,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice17 = Label(root,textvariable=amount15,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice18 = Label(root,textvariable=amount16,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))

myprice19 = Label(root,text="ราคา",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myprice20 = Label(root,textvariable=amount17,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice21= Label(root,textvariable=amount18,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice22 = Label(root,textvariable=amount19,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice23 = Label(root,textvariable=amount20,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice24 = Label(root,textvariable=amount21,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice25 = Label(root,textvariable=amount22,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))

myprice26 = Label(root,text="รวม",fg="black",bg="lightgreen",font=("thsarabunpsk 15"))

btn11 = Button(root,text="-",bg="salmon",command=minus1,)
btn12 = Button(root,text="+",bg="light green",command=add1)
btn13 = Button(root,text="-",bg="salmon",command=minus2)
btn14 = Button(root,text="+",bg="light green",command=add2)
btn15 = Button(root,text="-",bg="salmon",command=minus3)
btn16 = Button(root,text="+",bg="light green",command=add3)
btn17 = Button(root,text="-",bg="salmon",command=minus4)
btn18 = Button(root,text="+",bg="light green",command=add4)
btn19 = Button(root,text="-",bg="salmon",command=minus5)
btn20 = Button(root,text="+",bg="light green",command=add5)

btn21 = Button(root,text="หยิบใส่ตะกร้า",bg="lavender",font=("thsarabunpsk 20"),command=addproduct)

# #----------------------------------------------------------------------------------------------------------

amount23_cnt = 0
amount24_cnt = 0
amount25_cnt = 0
amount26_cnt = 0
amount27_cnt = 0
amount28_cnt = 0
amount29_cnt = 0
amount30_cnt = 0
amount31_cnt = 0
amount32_cnt = 0
amount33_cnt = 0


def add1():
    global amount23_cnt
    amount23_cnt +=1
    amount23.set(amount23_cnt)
    global amount28_cnt
    amount28_cnt +=40
    amount28.set(amount28_cnt)
    global amount11_cnt
    amount11_cnt +=40
    amount11.set(amount11_cnt)


    

def minus1():
    global amount23_cnt
    amount23_cnt -=1
    if amount23_cnt<=-1:
        amount23_cnt=0
    else: 
        amount23.set(amount23_cnt)
    global amount28_cnt
    amount28_cnt -=40
    if amount28_cnt<=-40:
        amount28_cnt=0
    else: 
        amount28.set(amount28_cnt)
    global amount11_cnt
    amount11_cnt -=40
    if amount11_cnt<=-40:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)


def add2():
    global amount24_cnt
    amount24_cnt +=1
    amount24.set(amount24_cnt)
    global amount29_cnt
    amount29_cnt +=40
    amount29.set(amount29_cnt)
    global amount11_cnt
    amount11_cnt +=40
    amount11.set(amount11_cnt)



def minus2():
    global amount24_cnt
    amount24_cnt -=1
    if amount24_cnt<=-1:
        amount24_cnt=0
    else: 
        amount24.set(amount24_cnt)
    global amount29_cnt
    amount29_cnt -=40
    if amount29_cnt<=-40:
        amount29_cnt=0
    else: 
        amount29.set(amount29_cnt)
    global amount11_cnt
    amount11_cnt -=40
    if amount11_cnt<=-40:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add3():
    global amount25_cnt
    amount25_cnt +=1
    amount25.set(amount25_cnt)
    global amount30_cnt
    amount30_cnt +=40
    amount30.set(amount30_cnt)
    global amount11_cnt
    amount11_cnt +=40
    amount11.set(amount11_cnt)

def minus3():
    global amount25_cnt
    amount25_cnt -=1
    if amount25_cnt<=-1:
        amount25_cnt=0
    else: 
        amount25.set(amount25_cnt)
    global amount30_cnt
    amount30_cnt -=40
    if amount30_cnt<=-40:
        amount30_cnt=0
    else: 
        amount30.set(amount30_cnt)
    global amount11_cnt
    amount11_cnt -=40
    if amount11_cnt<=-40:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add4():
    global amount26_cnt
    amount26_cnt +=1
    amount26.set(amount26_cnt)
    global amount31_cnt
    amount31_cnt +=45
    amount31.set(amount31_cnt)
    global amount11_cnt
    amount11_cnt +=45
    amount11.set(amount11_cnt)

def minus4():
    global amount26_cnt
    amount26_cnt -=1
    if amount26_cnt<=-1:
        amount26_cnt=0
    else: 
        amount26.set(amount26_cnt)
    global amount31_cnt
    amount31_cnt -=45
    if amount31_cnt<=-45:
        amount31_cnt=0
    else: 
        amount31.set(amount31_cnt)
    global amount11_cnt
    amount11_cnt -=45
    if amount11_cnt<=-45:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add5():
    global amount27_cnt
    amount27_cnt +=1
    amount27.set(amount27_cnt)
    global amount32_cnt
    amount32_cnt +=50
    amount32.set(amount32_cnt)
    global amount11_cnt
    amount11_cnt +=50
    amount11.set(amount11_cnt)

def minus5():
    global amount27_cnt
    amount27_cnt -=1
    if amount27_cnt<=-1:
        amount27_cnt=0
    else: 
        amount27.set(amount27_cnt)
    global amount32_cnt
    amount32_cnt -=50
    if amount32_cnt<=-55:
        amount32_cnt=0
    else: 
        amount32.set(amount32_cnt)
    global amount11_cnt
    amount11_cnt -=50
    if amount11_cnt<=-50:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def addproduct():
    tkinter.messagebox.showinfo("","หยิบสินค้าใส่ตะกร้าแล้ว")



amount23 = IntVar()
amount24 = IntVar()
amount25 = IntVar()
amount26 = IntVar()
amount27 = IntVar()
amount28 = IntVar()
amount29 = IntVar()
amount30 = IntVar()
amount31 = IntVar()
amount32 = IntVar()
amount33 = IntVar()


myfood15 = Label(root,text="ส้มตำ",fg="black",bg="lawngreen",font=("thsarabunpsk 40"))
myfood16 = Label(root,text="ตำลาว",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood17 = Label(root,text="ตำไทย",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood18 = Label(root,text="ตำแตง",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood19 = Label(root,text="ตำปูปลาร้า",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood20 = Label(root,text="ตำป่า",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood21 = Label(root,text="จำนวน",fg="black",bg="salmon",font=("thsarabunpsk 20"))

myprice27 = Label(root,textvariable=amount23,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice28 = Label(root,textvariable=amount24,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice29 = Label(root,textvariable=amount25,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice30 = Label(root,textvariable=amount26,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice31 = Label(root,textvariable=amount27,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))

myprice32 = Label(root,text="ราคา",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myprice33 = Label(root,textvariable=amount28,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice34 = Label(root,textvariable=amount29,bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice35 = Label(root,textvariable=amount30,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice36 = Label(root,textvariable=amount31,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice37 = Label(root,textvariable=amount32,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice38 = Label(root,textvariable=amount33,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))

myprice39 = Label(root,text="รวม",fg="black",bg="lightgreen",font=("thsarabunpsk 15"))

btn22 = Button(root,text="-",bg="salmon",command=minus1,)
btn23 = Button(root,text="+",bg="light green",command=add1)
btn24 = Button(root,text="-",bg="salmon",command=minus2)
btn25 = Button(root,text="+",bg="light green",command=add2)
btn26 = Button(root,text="-",bg="salmon",command=minus3)
btn27 = Button(root,text="+",bg="light green",command=add3)
btn28 = Button(root,text="-",bg="salmon",command=minus4)
btn29 = Button(root,text="+",bg="light green",command=add4)
btn30 = Button(root,text="-",bg="salmon",command=minus5)
btn31 = Button(root,text="+",bg="light green",command=add5)

btn32 = Button(root,text="หยิบใส่ตะกร้า",bg="lavender",font=("thsarabunpsk 20"),command=addproduct)

# #---------------------------------------------------------------------------------------------------------------
amount34_cnt = 0
amount35_cnt = 0
amount36_cnt = 0
amount37_cnt = 0
amount38_cnt = 0
amount39_cnt = 0
amount40_cnt = 0
amount41_cnt = 0
amount42_cnt = 0
amount43_cnt = 0
amount44_cnt = 0

def add1():
    global amount34_cnt
    amount34_cnt +=1
    amount34.set(amount34_cnt)
    global amount39_cnt
    amount39_cnt +=10
    amount39.set(amount39_cnt)
    global amount11_cnt
    amount11_cnt +=10
    amount11.set(amount11_cnt)


    

def minus1():
    global amount34_cnt
    amount34_cnt -=1
    if amount34_cnt<=-1:
        amount34_cnt=0
    else: 
        amount34.set(amount34_cnt)
    global amount39_cnt
    amount39_cnt -=10
    if amount39_cnt<=-10:
        amount39_cnt=0
    else: 
        amount39.set(amount39_cnt)
    global amount11_cnt
    amount11_cnt -=10
    if amount11_cnt<=-10:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)


def add2():
    global amount35_cnt
    amount35_cnt +=1
    amount35.set(amount35_cnt)
    global amount40_cnt
    amount40_cnt +=10
    amount40.set(amount40_cnt)
    global amount11_cnt
    amount11_cnt +=10
    amount11.set(amount11_cnt)



def minus2():
    global amount35_cnt
    amount35_cnt -=1
    if amount35_cnt<=-1:
        amount35_cnt=0
    else: 
        amount35.set(amount35_cnt)
    global amount40_cnt
    amount40_cnt -=10
    if amount40_cnt<=-10:
        amount40_cnt=0
    else: 
        amount40.set(amount40_cnt)
    global amount11_cnt
    amount11_cnt -=10
    if amount11_cnt<=-10:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add3():
    global amount36_cnt
    amount36_cnt +=1
    amount36.set(amount36_cnt)
    global amount41_cnt
    amount41_cnt +=10
    amount41.set(amount41_cnt)
    global amount11_cnt
    amount11_cnt +=10
    amount11.set(amount11_cnt)

def minus3():
    global amount36_cnt
    amount36_cnt -=1
    if amount36_cnt<=-1:
        amount36_cnt=0
    else: 
        amount36.set(amount36_cnt)
    global amount41_cnt
    amount41_cnt -=10
    if amount41_cnt<=-10:
        amount41_cnt=0
    else: 
        amount41.set(amount41_cnt)
    global amount11_cnt
    amount11_cnt -=10
    if amount11_cnt<=-10:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add4():
    global amount37_cnt
    amount37_cnt +=1
    amount37.set(amount37_cnt)
    global amount42_cnt
    amount42_cnt +=10
    amount42.set(amount42_cnt)
    global amount11_cnt
    amount11_cnt +=10
    amount11.set(amount11_cnt)

def minus4():
    global amount37_cnt
    amount37_cnt -=1
    if amount37_cnt<=-1:
        amount37_cnt=0
    else: 
        amount37.set(amount37_cnt)
    global amount42_cnt
    amount42_cnt -=10
    if amount42_cnt<=-10:
        amount42_cnt=0
    else: 
        amount42.set(amount42_cnt)
    global amount11_cnt
    amount11_cnt -=10
    if amount11_cnt<=-10:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

def add5():
    global amount38_cnt
    amount38_cnt +=1
    amount38.set(amount38_cnt)
    global amount43_cnt
    amount43_cnt +=10
    amount43.set(amount43_cnt)
    global amount11_cnt
    amount11_cnt +=10
    amount11.set(amount11_cnt)

def minus5():
    global amount38_cnt
    amount38_cnt -=1
    if amount38_cnt<=-1:
        amount38_cnt=0
    else: 
        amount38.set(amount38_cnt)
    global amount43_cnt
    amount43_cnt -=10
    if amount43_cnt<=-15:
        amount43_cnt=0
    else: 
        amount43.set(amount43_cnt)
    global amount11_cnt
    amount11_cnt -=10
    if amount11_cnt<=-10:
        amount11_cnt=0
    else: 
        amount11.set(amount11_cnt)

amount34 = IntVar()
amount35 = IntVar()
amount36 = IntVar()
amount37 = IntVar()
amount38 = IntVar()
amount39 = IntVar()
amount40 = IntVar()
amount41 = IntVar()
amount42 = IntVar()
amount43 = IntVar()
amount44 = IntVar()

myfood22 = Label(root,text="ของกินเล่น",fg="black",bg="lawngreen",font=("thsarabunpsk 40"))
myfood23 = Label(root,text="แคปหมู",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood24 = Label(root,text="แคปไก่",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood25 = Label(root,text="หมูหยอง",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood26 = Label(root,text="หมูยอ",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood27 = Label(root,text="ขนมจีน",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myfood28 = Label(root,text="จำนวน",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myprice40 = Label(root,textvariable=amount34,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice41 = Label(root,textvariable=amount35,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice42 = Label(root,textvariable=amount36,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice43 = Label(root,textvariable=amount37,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice44 = Label(root,textvariable=amount38,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice12 = Label(root,textvariable=amount11,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice45 = Label(root,text="ราคา",fg="black",bg="salmon",font=("thsarabunpsk 20"))
myprice46 = Label(root,textvariable=amount39,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice47= Label(root,textvariable=amount40,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice48 = Label(root,textvariable=amount41,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice49 = Label(root,textvariable=amount42,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice50 = Label(root,textvariable=amount43,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice51 = Label(root,textvariable=amount44,fg="black",bg="light gray",width=3,font=("thsarabunpsk 15"))
myprice52 = Label(root,text="รวม",fg="black",bg="lightgreen",font=("thsarabunpsk 15"))

btn33 = Button(root,text="-",bg="salmon",command=minus1,)
btn34 = Button(root,text="+",bg="light green",command=add1)
btn35 = Button(root,text="-",bg="salmon",command=minus2)
btn36 = Button(root,text="+",bg="light green",command=add2)
btn37 = Button(root,text="-",bg="salmon",command=minus3)
btn38 = Button(root,text="+",bg="light green",command=add3)
btn39 = Button(root,text="-",bg="salmon",command=minus4)
btn40 = Button(root,text="+",bg="light green",command=add4)
btn41 = Button(root,text="-",bg="salmon",command=minus5)
btn42 = Button(root,text="+",bg="light green",command=add5)

btn43 = Button(root,text="หยิบใส่ตะกร้า",bg="lavender",font=("thsarabunpsk 20"),command=addproduct)


billarea=Frame(root,bd=10,relief=GROOVE,bg="#ffffff")
bill_title=Label(billarea,text="Bill",font=("Times",19),fg="#ffffff",bd=7,bg="#d39c2e",relief=GROOVE)
bill_title.pack(fill=X)
scrol_y=Scrollbar(billarea,orient=VERTICAL)
txtarea=Text(billarea,font=("Times",14),yscrollcommand=scrol_y.set)

scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH,expand=2)
btn_1111 = Button(root,text="-",bg="salmon",command=pay_1)
GUI.mainloop()








from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql
def insert():
    a=ea.get()
    b=eb.get()
    c=ec.get()
    d=ed.get()
    if(a=="" or b=="" or c=="" or d==""):
        messagebox.showinfo("IN mycursor.execute(sql,val)SERT STATUS","All Fields Are Required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="python-tkinter")
        mycursor=con.cursor()
        sql="insert into bank(a,b,c,d)values(%s,%s,%s,%s)"
        val=(a,b,c,d)
       
        con.commit()
        ea.delete(0,'end')
        eb.delete(0,'end')
        ec.delete(0,'end')
        ed.delete(0,'end')
        messagebox.showinfo("INSERT STATUS","Inserted sucessfully")
        con.close()
def delete():
    print("hi")
def update():
    print("bye")
def get():
    print("welcome")        
root=Tk()
root.geometry("600x300")
root.title("Banking Management system")
a=Label(root,text="Enter name",font=('bold',10),fg='blue')
a.place(x=20,y=30)
b=Label(root,text="Enter acc no",font=('bold',10),fg='orange')
b.place(x=20,y=60)
c=Label(root,text="Enter mobile no",font=('bold',10),fg='red')
c.place(x=20,y=90)
d=Label(root,text="Enter Gmail",font=('bold',10),fg='green')
d.place(x=20,y=120)
ea=Entry()
ea.place(x=120,y=30)
eb=Entry()
eb.place(x=120,y=60)
ec=Entry()
ec.place(x=120,y=90)
ed=Entry()
ed.place(x=120,y=120)
i=Button(root,text='Submit', font=('italic',10),command=insert)
i.place(x=20,y=150)
j=Button(root,text='Delete', font=('italic',10),command=delete)
j.place(x=80,y=150)
k=Button(root,text='Update', font=('italic',10),command=update)
k.place(x=140,y=150)
l=Button(root,text='Get', font=('italic',10),command=get)
l.place(x=200,y=150)
root.mainloop()
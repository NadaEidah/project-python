#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:31:33 2019

@author: nada
"""

#Project 3
print('-------- 1--------------')

import sqlite3
conn = sqlite3.connect('OrgDB.db')
from tkinter import *
from tkinter import Tk
from tkinter import scrolledtext
from tkinter import messagebox

root=Tk()

"""
c=conn.cursor()

c.execute('''CREATE TABLE EmployeesTable
          (EmploeeNumber int, 
          EmploeeName text,
          EmployeeGender text, 
          EmployeeNationality text, 
          EmployeeDateofBirth text, 
          EmployeeAddress text,
          EmployeeDepartment text,
          EmployeeSalary  real)''')


conn.commit()
conn.close()
"""

print('-------- 2--------------')

def add():
    
    def save():
        c = conn.cursor()
        c.execute("INSERT INTO EmployeesTable VALUES(?,?,?,?,?,?,?,?)",(val1.get(),val2.get(),val3.get(),val4.get(),val5.get(),val6.get(),val7.get(),val8.get()))
        conn.commit()
        messagebox.showinfo("thanks","Add It Successfully")
        
    addwin=Toplevel(root)
    addwin.title(' add')
    
    val1=IntVar()
    val2=StringVar()
    val3=StringVar()
    val4=StringVar()
    val5=StringVar()
    val6=StringVar() 
    val7=StringVar()
    val8=IntVar()
    
    number=Label(addwin,text="Emploee Number").grid(row=0,sticky=E)
    e1=Entry(addwin,textvariable=val1).grid(row=0,column=1)
    
    name=Label(addwin,text="Emploee Name").grid(row=1,sticky=E)
    e2=Entry(addwin,textvariable=val2).grid(row=1,column=1)
     
    gender=Label(addwin,text="Employee Gender").grid(row=2,sticky=E)
    e3=Entry(addwin,textvariable=val3).grid(row=2,column=1)
    
    nationality=Label(addwin,text="Employee Nationality").grid(row=3,sticky=E)
    e4=Entry(addwin,textvariable=val4).grid(row=3,column=1)
    
    dateofbirth=Label(addwin,text="Employee Birthday").grid(row=4,sticky=E)
    e5=Entry(addwin,textvariable=val5).grid(row=4,column=1)
    
    address=Label(addwin,text="Employee Address").grid(row=5,sticky=E)
    e6=Entry(addwin,textvariable=val6).grid(row=5,column=1)
    
    deparment=Label(addwin,text="Employee Department").grid(row=6,sticky=E)
    e7=Entry(addwin,textvariable=val7).grid(row=6,column=1)
    
    salary=Label(addwin,text="Employee Salary").grid(row=7,sticky=E)
    e8=Entry(addwin,textvariable=val8).grid(row=7,column=1)
     
     
    button=Button(addwin,text="Save",command=save).grid(row=8,sticky=E)
    
def view():
    c = conn.cursor()
    c.execute("SELECT * FROM EmployeesTable")
    
    addwin=Toplevel(root)
    addwin.title('view')
    txt = scrolledtext.ScrolledText(addwin, width=100, height=100)
    
    for row in c:
        txt.insert(END,row)
        txt.insert(END,"\n")
    
    txt.yview(END)
    txt.pack()
    conn.commit() 

top=Menu(root)
root.config(menu=top)
file=Menu(top,tearoff=0)
file.add_command(label='Add',command=add)
file.add_command(label='view',command=view)
top.add_cascade(label='Employee',menu=file)
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()

root.geometry("400x200+680+300")
root.mainloop()

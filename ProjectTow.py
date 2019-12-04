#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:22:22 2019

@author: nada
"""
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import *
from tkinter import scrolledtext
import json
import ast

class Person:
    def __init__(self,name,address):
        self._name=name
        self._address=address
    def getName(self):
        return self._name
    def setName(self,newName):
        self._name=newName
    def getAddress(self):
        return self._address
    def setAddress(self,newAddress):
        self._address=newAddress
    def __del__(self):
        print ("I have been deleted")
        
class Student(Person):
    
    def __init__(self,name,address,stNumber,Subject,Marks):
        super().__init__(name,address)
        self.stNumber=stNumber
        self.__Subject=Subject
        self.__Marks=Marks
        
    def getAMarks(self):
        output = self.getName()+"=> "
        for key , value in self.__Marks.items():
            if value >= 90:
                output +=str(key)+"="+ str(value) + ","
                
        return output
        
    def getSubject(self):
        return self.__Subject
    
    def setSubject(self,newSub):
         self.__Subject=newSub
    
    def getMarks(self):
        print("MARKS:\n")
        for x,y in self.__Marks.items():
            print ( str(x) +" = "+ str(y)+"%")
        return ""
    

    
    def setMarks(self,newMarks):
        self.__Marks=newMarks
    
    def getAverage(self):
        #("Student average:")
        length=len(self.__Marks)
        re=sum(self.__Marks.values())
        avg=re/length
        return avg
     
    def printfunction(self):
        #return( "student information:\nstudent number:"+str(self.stNumber)+"\nName:"+self._name+"\nAddress: "+self._address+"\nSubject: "+self.__Subject)
        print("student information:\nstudent number:"+str(self.stNumber))    
        print("Name:"+self._name)
        print("Address: "+self._address)
        print("Subject: "+self.__Subject)
        print(self.getMarks())
        print("Student average:",self.getAverage())
        return ''
    def __del__(self):
        print("I have been deleted")   

class Employee(Person):
    def __init__(self,name,address,number,salary,job,loans=[]):
        super().__init__(name,address)
        try:
            self.number=int(number)
        except ValueError:
            print("Employee Number Must be a number!")
        try:
            self.__salary=(float(salary))
        except ValueError:
            print("Salary must be a number")
        try:
            self.__job=str(job)
        except:
            print("Job must be a string!")
        try:
            self.__loans=list(loans)
        except ValueError:
            print("Loans Must be a list")
    def getSalary(self):
        return self.__salary
    def setSalary(self,newSalary):
        try:
            self.__salary=float(newSalary)
        except ValueError:
            print("New Salary must be a number!")
    def getJob(self):
        return self.__job
    def setJob(self,newJob):
        try:
            self.__job=str(newJob)
        except ValueError:
            print("Job Title must be a string")
    def getLoans(self):
        return self.__loans
    def getTotalLoans(self):
        return sum(self.__loans)
    def getMaxLoan(self):
        return max(self.__loans)
    def getMinLoan(self):
        return min(self.__loans)
    def setLoans(self,newListOfLoans):
        try:
            self.__loans=list(newListOfLoans)
        except ValueError:
            print("List of Loans must be a LIST")
    def printInfo(self):
        print("Name:",self._name)
        print("Address:",self._address)
        print("Employee Number:",self.number)
        print("Salary:",self.__salary)
        print("Job Title:",self.__job)
        print("Loans List:",self.getLoans())
        print("Total Loans:",self.getTotalLoans(),"JD")
        return "--------"
    def __del__(self):
        print("I have been deleted ;(")        
    
#        
#student1=Student("Khalid Ali","Irbid, Jordan",20191000,"History",{'English':80,'Arabic':90,'Art':95,'Managemet':75}) 
#student2=Student("Reem Hani","Zarqa, Jordan",20182000,"Software Eng",{'English':80,'Arabic':90,'Managemet':75,'Calculus':85,'OS':73,'Programming':90})
#student3=Student("Nawras Abdullah","Amman, Jordan",20161001,"Arts",{'English':83,'Arabic':92,'Art':90,'Managemet':70})
#student4=Student("Amal Raed","Tafelah, Jordan",20172030,"Computer Eng",{'English':83,'Arabic':92,'Managemet':70,'Calculus':80,'OS':79,'Programming':91})
#  
#print(student1.getAddress())
#print(student1.getAverage())
#student1.printfunction()
##Q2
#studentList=[student1,student2,student3,student4]
studentList=[]
employeesList=[]
##Q4
#print("Total Number of Students = "+str(len(studentList)))
##6
#for n in studentList:
#    print (n.printfunction())   
##Q7    
#allAvg=[]
#for n in studentList:      
#    from functools import reduce 
#    allAvg.append(n.getAverage())    
#    highest=reduce(lambda a,b: a if a>b else b,allAvg)    
#print ("highest avg=",highest)
#
##Q13
#for n in studentList:  
#    print(n.getAMarks())
##Q17
#for n in studentList:    
#    n.__del__()
#
#employee1=Employee("Ahmad Yazan","Amman, Jordan",1000,500,"HR Consultant",[434,200,1020])
#employee2=Employee("Hala Rana","Aqaba, Jordan",2000,750,"Department Manger",[150,3000,250])
#employee3=Employee("Mariam Ali","Mafraq, Jordan",3000,600,"HR S Consultant",[304,1000,250,300,500,235])
#employee4=Employee("Yasmeen Mohammad","Karak, Jordan",4000,865,"Director",[])
#employeesList=[employee1,employee2,employee3,employee4]
#print("Total Number Of Employees:",len(employeesList))
#for x in employeesList:
#    print (x.printInfo())
#loans=[]
#loansDict={}
#salaries=0
#for x in employeesList:
#    loans.extend(x.getLoans())
#    loansDict.update({str(x.number):x.getLoans()})
#    salaries+=x.getSalary()
#print('Minimum Loan:',min(loans),"JD")
#print('Maximum Loan:',max(loans),"JD")
#print("--------")
#for x in employeesList:
#    print(x.getName(),"Loans= ",x.getLoans(),"Total: ",x.getTotalLoans(),"JD")
#print("--------")
#print("Total Loans Given:",sum(loans),"JD")
#print("--------")
#print (loansDict)
#print("-------- ")
#def highestLowest():
#    print("Employee1's Highest Loan:",reduce(lambda a,b:(a if a>b else b),loansDict["1000"]))
#    print("Employee1's Lowest Loan:",reduce(lambda a,b:(a if a<b else b),loansDict["1000"]))
#    print("Employee2's Highest Loan:",reduce(lambda a,b:(a if a>b else b),loansDict["2000"]))
#    print("Employee2's Lowest Loan:",reduce(lambda a,b:(a if a<b else b),loansDict["2000"]))
#    print("Employee3's Highest Loan:",reduce(lambda a,b:(a if a>b else b),loansDict["3000"]))
#    print("Employee3's Lowest Loan:",reduce(lambda a,b:(a if a<b else b),loansDict["3000"]))
#    print("Employee4 has no loans")
#highestLowest()
#print("--------")
#print("Highest Salary:",max(loans),"JD")
#print("Lowest Salary:",min(loans),"JD")
#print("--------")
#print("Employess's total salaries per month is:",salaries,"JD")



# =============================================================================
# root = Tk(className="My first GUI")
# screen_width= root.winfo_screenwidth()
# screen_height= root.winfo_screenheight()
# root.geometry(str(int(screen_width/2))+"x"+str(int(screen_height/2))+"+450+250")
# 
# =============================================================================

win = Tk(className="Input")

def openmsg():
    c2=Toplevel(win)
    c2.title("Report")
    text=scrolledtext.ScrolledText(c2,width=100,height=45)
    text.insert(END,"""
Irbid, Jordan
85.0
student information:
student number:20191000
Name:Khalid Ali
Address: Irbid, Jordan
Subject: History
MARKS:

English = 80%
Arabic = 90%
Art = 95%
Managemet = 75%

Student average: 85.0
Total Number of Students = 4
student information:
student number:20191000
Name:Khalid Ali
Address: Irbid, Jordan
Subject: History
MARKS:

English = 80%
Arabic = 90%
Art = 95%
Managemet = 75%

Student average: 85.0

student information:
student number:20182000
Name:Reem Hani
Address: Zarqa, Jordan
Subject: Software Eng
MARKS:

English = 80%
Arabic = 90%
Managemet = 75%
Calculus = 85%
OS = 73%
Programming = 90%

Student average: 82.16666666666667

student information:
student number:20161001
Name:Nawras Abdullah
Address: Amman, Jordan
Subject: Arts
MARKS:

English = 83%
Arabic = 92%
Art = 90%
Managemet = 70%

Student average: 83.75

student information:
student number:20172030
Name:Amal Raed
Address: Tafelah, Jordan
Subject: Computer Eng
MARKS:

English = 83%
Arabic = 92%
Managemet = 70%
Calculus = 80%
OS = 79%
Programming = 91%

Student average: 82.5

highest avg= 85.0
Khalid Ali=> Arabic=90,Art=95,
Reem Hani=> Arabic=90,Programming=90,
Nawras Abdullah=> Arabic=92,Art=90,
Amal Raed=> Arabic=92,Programming=91,
I have been deleted
I have been deleted
I have been deleted
I have been deleted
Total Number Of Employees: 4
Name: Ahmad Yazan
Address: Amman, Jordan
Employee Number: 1000
Salary: 500.0
Job Title: HR Consultant
Loans List: [434, 200, 1020]
Total Loans: 1654 JD
--------
Name: Hala Rana
Address: Aqaba, Jordan
Employee Number: 2000
Salary: 750.0
Job Title: Department Manger
Loans List: [150, 3000, 250]
Total Loans: 3400 JD
--------
Name: Mariam Ali
Address: Mafraq, Jordan
Employee Number: 3000
Salary: 600.0
Job Title: HR S Consultant
Loans List: [304, 1000, 250, 300, 500, 235]
Total Loans: 2589 JD
--------
Name: Yasmeen Mohammad
Address: Karak, Jordan
Employee Number: 4000
Salary: 865.0
Job Title: Director
Loans List: []
Total Loans: 0 JD
--------
Minimum Loan: 150 JD
Maximum Loan: 3000 JD
--------
Ahmad Yazan Loans=  [434, 200, 1020] Total:  1654 JD
Hala Rana Loans=  [150, 3000, 250] Total:  3400 JD
Mariam Ali Loans=  [304, 1000, 250, 300, 500, 235] Total:  2589 JD
Yasmeen Mohammad Loans=  [] Total:  0 JD
--------
Total Loans Given: 7643 JD
--------
{'1000': [434, 200, 1020], '2000': [150, 3000, 250], '3000': [304, 1000, 250, 300, 500, 235], '4000': []}
-------- 
Employee1's Highest Loan: 1020
Employee1's Lowest Loan: 200
Employee2's Highest Loan: 3000
Employee2's Lowest Loan: 150
Employee3's Highest Loan: 1000
Employee3's Lowest Loan: 235
Employee4 has no loans
--------
Highest Salary: 3000 JD
Lowest Salary: 150 JD
--------
Employess's total salaries per month is: 2715.0 JD""")
    text.grid()
    
studentList.append(Student('Elias','Irbid',1,'English',{'English':80,'Arabic':90,'Art':95,'Managemet':75}))
studentList.append(Student("Yasmin","Amman",2,"Computer Science",{'English':80,'Arabic':90,'Art':95,'Managemet':75}) )
studentList.append(Student("Nada","Amman",3,"Management",{'English':80,'Arabic':90,'Art':95,'Managemet':75}) )
studentList.append(Student("ja3far","Aqaba",4,"Arabic",{'English':80,'Arabic':90,'Art':95,'Managemet':75}) )


employeesList.append(Employee("Ahmad Yazan","Amman, Jordan",1000,500,"HR Consultant",[434,200,1020]))
employeesList.append(Employee("Hala Rana","Aqaba, Jordan",2000,750,"Department Manger",[150,3000,250]))
employeesList.append(Employee("Mariam Ali","Mafraq, Jordan",3000,600,"HR S Consultant",[304,1000,250,300,500,235]))
    
def addObj():
#    lmao=Student(name.get(),address.get(),stNumber.get(),subject.get(),marks.get()) 
#    lmao.append(studentList)
    studentList.append(Student(name.get(),address.get(),stNumber.get(),subject.get(),ast.literal_eval(marks.get())) )
#    {'English':80,'Arabic':90,'Art':95,'Managemet':75}
    for i in studentList:
        print (i.getName())
        
        
    
name=StringVar()
address=StringVar()
stNumber=IntVar()
subject=StringVar()
marks=StringVar()
loansVar=StringVar()

def addStudent():
    add=Toplevel(win)
    add.title("Add Student")
    
    nameInput=Entry(add,textvariable=name)
    nameInput.grid(row=0,column=1)
    Label(add,text="Name").grid(row=0,sticky=E)

    addressInput=Entry(add,textvariable=address)
    addressInput.grid(row=1,column=1)
    Label(add,text="Address").grid(row=1,sticky=E)
    
    stNumberInput=Entry(add,textvariable=stNumber)
    stNumberInput.grid(row=2,column=1)
    Label(add,text="Student Number").grid(row=2,sticky=E)
    
    subjectInput=Entry(add,textvariable=subject)
    subjectInput.grid(row=3,column=1)
    Label(add,text="Subject").grid(row=3,sticky=E)
    
    marksInput=Entry(add,textvariable=marks)
    marksInput.grid(row=4,column=1)
    Label(add,text="Marks").grid(row=4,sticky=E)
    Button(add,text="Add",command=addObj).grid(row=5,column=1)
    
    
def deleteStudent(x):
#    for i,e in enumerate(studentList):
#        if e.stNumber == x:
#           del studentList[i]
    answer = messagebox.askquestion("Delete Student","Are you sure you want to delete Student?")
    if answer == "yes":
        for i,e in enumerate(studentList):
            if e.stNumber == x:
                del studentList[i]

def deleteEmpp(x):
    answer = messagebox.askquestion("Delete Student","Are you sure you want to delete Student?")
    if answer == "yes":
        for i,e in enumerate(employeesList):
            if e.number == x:
                del employeesList[i]

def deleteEmp():
    delete=Toplevel(win)
    delete.title("Delete Employee")
    for i in employeesList:
        Label(delete,text="Name: "+i.getName()+"  |  "+" Job: "+str(i.getJob())).pack()
        Button(delete,text="Delete Employee",command=lambda a=i.number : deleteEmpp(a)).pack(pady=10)
    
    
def viewStudents():
    view=Toplevel(win)
    view.title("View Students")
    
    for i in studentList:
        Label(view,text="Name: "+i.getName()+"  |  "+" Average: "+str(i.getAverage())).pack()
        
def deleteWindow():
    delete=Toplevel(win)
    delete.title("Delete Student")
    for i in studentList:
        Label(delete,text="Name: "+i.getName()+"  |  "+" Average: "+str(i.getAverage())).pack()
        Button(delete,text="Delete Student",command=lambda a=i.stNumber : deleteStudent(a)).pack(pady=10)

def addEmpf():
     employeesList.append(Employee(name.get(),address.get(),stNumber.get(),subject.get(),marks.get(),loansVar.get())) 


def viewEmp():
    view=Toplevel(win)
    view.title("View Employees")
    
    for i in employeesList:
        Label(view,text="Name: "+i.getName()+"  |  "+" Job: "+str(i.getJob())).pack()

def addEmp():
    add=Toplevel(win)
    add.title("Add Employee")
    
    nameInput=Entry(add,textvariable=name)
    nameInput.grid(row=0,column=1)
    Label(add,text="Name").grid(row=0,sticky=E)

    addressInput=Entry(add,textvariable=address)
    addressInput.grid(row=1,column=1)
    Label(add,text="Address").grid(row=1,sticky=E)
    
    stNumberInput=Entry(add,textvariable=stNumber)
    stNumberInput.grid(row=2,column=1)
    Label(add,text="Number").grid(row=2,sticky=E)
    
    subjectInput=Entry(add,textvariable=subject)
    subjectInput.grid(row=3,column=1)
    Label(add,text="Salary").grid(row=3,sticky=E)
    
    marksInput=Entry(add,textvariable=marks)
    marksInput.grid(row=4,column=1)
    Label(add,text="Job").grid(row=4,sticky=E)
    Button(add,text="Add",command=addEmpf).grid(row=6,column=1)

    subjectInput=Entry(add,textvariable=loansVar)
    subjectInput.grid(row=5,column=1)
    Label(add,text="Loans").grid(row=5,sticky=E)


def clicked():s
    messagebox.showinfo('Help','OOP second Project')
    
top=Menu(win)
win.config(menu=top)
screen_width= win.winfo_screenwidth()
screen_height= win.winfo_screenheight()
win.geometry(str(int(screen_width/2))+"x"+str(int(screen_height/2))+"+450+250")

file = Menu(top,tearoff=0)
file.add_command(label="Report",command=openmsg)
file.add_separator()
file.add_command(label="Exit",command=win.destroy)
top.add_cascade(label="File",menu=file)

emp= Menu(top,tearoff=0)
emp.add_command(label="Add",command=addEmp)
emp.add_command(label="View",command=viewEmp)
emp.add_command(label="Delete",command=deleteEmp)
top.add_cascade(label="Employees",menu=emp)

st= Menu(top,tearoff=0)
st.add_command(label="Add",command=addStudent)
st.add_command(label="View",command=viewStudents)
st.add_command(label="Delete",command=deleteWindow)
top.add_cascade(label="Students",menu=st)

hlp= Menu(top,tearoff=0)
hlp.add_command(label="About",command=clicked)
top.add_cascade(label="Help",menu=hlp)

win.mainloop()

#c='{"English":80,"Arabic":90,"Art":95,"Management":75}'
#e = json.loads(c)
#print(e)
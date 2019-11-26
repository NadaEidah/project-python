#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:33:59 2019

@author: nada
"""
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
    
        
student1=Student("Khalid Ali","Irbid, Jordan",20191000,"History",{'English':80,'Arabic':90,'Art':95,'Managemet':75}) 
student2=Student("Reem Hani","Zarqa, Jordan",20182000,"Software Eng",{'English':80,'Arabic':90,'Managemet':75,'Calculus':85,'OS':73,'Programming':90})
student3=Student("Nawras Abdullah","Amman, Jordan",20161001,"Arts",{'English':83,'Arabic':92,'Art':90,'Managemet':70})
student4=Student("Amal Raed","Tafelah, Jordan",20172030,"Computer Eng",{'English':83,'Arabic':92,'Managemet':70,'Calculus':80,'OS':79,'Programming':91})
  
print(student1.getAddress())
print(student1.getAverage())
student1.printfunction()
#Q2
studentList=[student1,student2,student3,student4]
#Q4
print("Total Number of Students = "+str(len(studentList)))
#6
for n in studentList:
    print (n.printfunction())   
#Q7    
allAvg=[]
for n in studentList:      
    from functools import reduce 
    allAvg.append(n.getAverage())    
    highest=reduce(lambda a,b: a if a>b else b,allAvg)    
print ("highest avg=",highest)

#Q13
for n in studentList:  
    print(n.getAMarks())
#Q17
for n in studentList:    
    n.__del__()

employee1=Employee("Ahmad Yazan","Amman, Jordan",1000,500,"HR Consultant",[434,200,1020])
employee2=Employee("Hala Rana","Aqaba, Jordan",2000,750,"Department Manger",[150,3000,250])
employee3=Employee("Mariam Ali","Mafraq, Jordan",3000,600,"HR S Consultant",[304,1000,250,300,500,235])
employee4=Employee("Yasmeen Mohammad","Karak, Jordan",4000,865,"Director",[])
employeesList=[employee1,employee2,employee3,employee4]
print("Total Number Of Employees:",len(employeesList))
for x in employeesList:
    print (x.printInfo())
loans=[]
loansDict={}
salaries=0
for x in employeesList:
    loans.extend(x.getLoans())
    loansDict.update({str(x.number):x.getLoans()})
    salaries+=x.getSalary()
print('Minimum Loan:',min(loans),"JD")
print('Maximum Loan:',max(loans),"JD")
print("--------")
for x in employeesList:
    print(x.getName(),"Loans= ",x.getLoans(),"Total: ",x.getTotalLoans(),"JD")
print("--------")
print("Total Loans Given:",sum(loans),"JD")
print("--------")
print (loansDict)
print("-------- ")
def highestLowest():
    print("Employee1's Highest Loan:",reduce(lambda a,b:(a if a>b else b),loansDict["1000"]))
    print("Employee1's Lowest Loan:",reduce(lambda a,b:(a if a<b else b),loansDict["1000"]))
    print("Employee2's Highest Loan:",reduce(lambda a,b:(a if a>b else b),loansDict["2000"]))
    print("Employee2's Lowest Loan:",reduce(lambda a,b:(a if a<b else b),loansDict["2000"]))
    print("Employee3's Highest Loan:",reduce(lambda a,b:(a if a>b else b),loansDict["3000"]))
    print("Employee3's Lowest Loan:",reduce(lambda a,b:(a if a<b else b),loansDict["3000"]))
    print("Employee4 has no loans")
highestLowest()
print("--------")
print("Highest Salary:",max(loans),"JD")
print("Lowest Salary:",min(loans),"JD")
print("--------")
print("Employess's total salaries per month is:",salaries,"JD")    


   
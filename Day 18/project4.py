#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:00:18 2019

@author: nada
"""

print("‫‪Project‬‬ ‫‪4‬‬")


from flask import Flask,redirect,url_for,request,render_template
import sqlite3

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/success",methods=["POST"])
def success():
    if request.method=="POST":
        try:
            request.form['username'] == 'nada' and request.form['password'] == '123'
            msg="login success"
        except:
            msg="worng user name and password"
        finally:
            return render_template("success.html", msg=msg)
 
           
@app.route("/logout")
def logout():
        return render_template("login.html")    
    
'''  
@app.route("/profile")
def profile():
    if 'name' in session:
        name=session['name']
        return render_template("profile.html", name=name)
'''    
@app.route("/department")
def department():
    con=sqlite3.connect('org.db')
    con.row_factory=sqlite3.Row 
    
    cur=con.cursor()
    res=cur.execute("select * from departments")
    rows=cur.fetchall();
    return render_template("deprList.html",rows=rows)

@app.route("/addDpratment")
def addDpratment():
    return render_template("add.html");

@app.route("/newDepartment", methods=["POST","GET"])
def newDepartment():
    msg="msg"
    if request.method == 'POST':
        try:
            #department_id=request.form['did']
            department_name=request.form['department_name']
            location_id=request.form['location_id']
            
            with sqlite3.connect('org.db') as con:
                cur=con.cursor()
                cur.execute("INSERT INTO departments (department_name,location_id) VALUES(?,?)",(department_name,location_id))

                con.commit()
                msg="Employee successfully added"
        except:
            con.rollback()
            msg="we can not add the employee to the list"
        
        finally:
            return render_template("deprList.html", msg=msg)
            con.close()
            
@app.route('/viewDepartment')
def viewDepartment():
    con=sqlite3.connect('org.db')
   
    
    cur=con.cursor()
    cur.execute('select * from departments')
    
    rows=cur.fetchall()
    return render_template("view.html",rows=rows)


  
'''
@app.route("/addEmployee")
def addEmployee():
    return render_template("adde.html");

@app.route("/newEmployee", methods=["POST","GET"])
def newEmployee():
    msg="msg"
    if request.method == 'POST':
        try:
            employee_id=request.form['employee_id']
            first_name=request.form['first_name']
            email=request.form['email']
            phone_number=request.form['phone_number']
            hire_data=request.form['hire_data']
            job_id=request.form['job_id']
            salary=request.form['salary']
            department_id=request.form['department_id']
            
            with sqlite3.connect('org.db') as con:
                cur=con.cursor()
                cur.execute("INSERT INTO employees (employee_id,first_name,email,phone_number,hire_data,job_id,salary,department_id) VALUES(?,?,?,?,?,?,?,?)",(employee_id,first_name,email,phone_number,hire_data,job_id,salary,department_id))

                con.commit()
                msg="Employee successfully added"
        except:
            con.rollback()
            msg="we can not add the employee to the list"
        
        finally:
            return render_template("success3.html", msg=msg)
            con.close()
'''
@app.route('/viewEmployee', methods=["POST","GET"])
def viewEmployee():
    if request.method == "POST":
        department_id=request.form["info"]
        with sqlite3.connect("org.db") as con:
            cur = con.cursor()
            cur.execute("select * from employees where department_id = ?",department_id)
            rows = cur.fetchall()
        return render_template("view2.html",rows=rows)
#done to here-----------------------------------------------   
@app.route("/updateform",methods=["POST","GET"])
def updateform():
    if request.method == "POST":
        department_id=request.form["id"]
        with sqlite3.connect("org.db") as con:
            cur = con.cursor()
            cur.execute("select * from departments")
            dep = cur.fetchall()
        return render_template("updateEmple.html",dep=department_id)
    
@app.route('/updateEmployee', methods=["POST","GET"])
def updateEmployee():
        if request.method == 'POST':
            first_name=request.form['first_name']
            email=request.form['email']
            phone_number=request.form['phone_number']
            hire_data=request.form['hire_data']
            job_id=request.form['job_id']
            salary=request.form['salary']
            department_id=request.form['department_id']
          
            allInfo=(employee_id,first_name,email,phone_number,hire_data,job_id,salary,department_id)
            
            with sqlite3.connect('org.db') as con:
                cur=con.cursor()
                cur.execute("update employees set first_name = ?,last_name=?,email=?,phone_number=?,hire_date=?,job_id=?,salary=?,department_id=? where employee_id = ?", allInfo)

                con.commit()
                
            return render_template("success.html")

if __name__=='__main__':
    app.run()
       
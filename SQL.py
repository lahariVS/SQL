from tkinter import *
import sqlite3
import time
r=Tk()
r.title('Account')
conn=sqlite3.connect('acc.db')
c=conn.cursor()
r.geometry("400x400")
#c.execute("CREATE TABLE Account(fname varchar(15),password varchar(15),email varchar(15),phone varchar(10))")
#c.execute("CREATE TABLE c(n varchar(15),p varchar(15))")

def signup():
  root=Tk()
  conn=sqlite3.connect('acc.db')
  c=conn.cursor()
  root.title('Sign Up!')
  root.geometry("400x400")
  fname=Entry(root,width=30)
  fname.grid(row=0,column=1)
  
  password=Entry(root,width=30)
  password.grid(row=1,column=1)
  
  email=Entry(root,width=30)
  email.grid(row=2,column=1)
  
  phone=Entry(root,width=30)
  phone.grid(row=3,column=1)
  
  #delete_box=Entry(root,width=30)
  #delete_box.grid(row=9,column=1)

  name_label=Label(root,text="User Name")
  name_label.grid(row=0,column=0)
  password_label=Label(root,text="Password")
  password_label.grid(row=1,column=0)
  email_label=Label(root,text="Email ID")
  email_label.grid(row=2,column=0)
  phone_label=Label(root,text="Phone Number")
  phone_label.grid(row=3,column=0)
  
  """def delete():
    conn=sqlite3.connect('acc.db')
    c=conn.cursor()
    c.execute("DELETE FROM Account WHERE oid="+delete_box.get())
    conn.commit()"""
   
  
  
  def validate():
    n=fname.get()
    p=password.get()
    e=email.get()
    ph=phone.get()
    uc=0
    lc=0
    nc=0
    k=0
    j=0
    g=0
    res=0
    z1=0
    z2=0
    z3=0
    z4=0
    #User Name
    while(len(n)==0 or n[0].isdigit() or len(n)<8):
      z1=1
      fname.delete(0,END)
      
      lab1_label=Label(root,text="Invalid Input")
      lab1_label.grid(row=10,column=0,columnspan=4)
      
      break
    #Password
    while(res<4):
      res=0
      if(len(p)>8):
        res+=1
      for i in range(len(p)):
        if(p[i].islower()):
          uc=1
        elif(p[i].isupper()):
          lc=1
        elif(p[i].isdigit()):
          nc=1
      if(uc==1 and lc==1 and nc==1):
        res+=3
      if(res!=4):
        password.delete(0,END)
        
        lab1_label=Label(root,text="Invalid Input")
        lab1_label.grid(row=10,column=0,columnspan=4)
        
        z2=1
      else:
        break
      break
    #Email ID
    while(len(e)<8):
      email.delete(0,END)
      
      lab1_label=Label(root,text="Invalid Input")
      lab1_label.grid(row=10,column=0,columnspan=4)
      
      z3=1
      break
    while(len(e)>8):
      for j in range(len(e)):
        if(e[j]=='@'):
          k=1
      if(k!=1):
        email.delete(0,END)
        
        lab1_label=Label(root,text="Invalid Input")
        lab1_label.grid(row=10,column=0,columnspan=4)
        
        z3=1
      break
    #Phone Number
    while(len(ph)<10):
      phone.delete(0,END)
      
      lab1_label=Label(root,text="Invalid Input")
      lab1_label.grid(row=10,column=0,columnspan=4)
      z4=1
      break
    while(len(ph)>10):
      g=0
      for x in range(len(ph)):
        if(ph[x].isdigit()):
          g+=1
      if(g!=10):
        phone.delete(0,END)
        
        lab1_label=Label(root,text="Invalid Input")
        lab1_label.grid(row=10,column=0,columnspan=4)
        
        z4=1
        break
      break
    if(z1==0 and z2==0 and z3==0 and z4==0):
      submit()
      
      lab1_label=Label(root,text="Congratulations Account Created")
      lab1_label.grid(row=10,column=0,columnspan=4)
    
      
  def submit():
    conn=sqlite3.connect('acc.db')
    c=conn.cursor()
    c.execute("INSERT INTO Account VALUES(:fname,:password,:email,:phone)",
    {
      'fname' : fname.get(),
      'password' : password.get(),
      'email' : email.get(),
      'phone' : phone.get(),
    })
    conn.commit()
    conn.close()
    fname.delete(0,END)
    password.delete(0,END)
    email.delete(0,END)
    phone.delete(0,END)

  def display():
    conn=sqlite3.connect('acc.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM Account")
    records=c.fetchall()
    pr=''
    for r in records:
      pr+=str(r)+"\n"

    q_label=Label(root,text=pr)
    q_label.grid(row=10,column=0,columnspan=4)
    
  
  check_btn=Button(root,text="Submit",command=validate)
  check_btn.grid(row=5,column=1)


  """display_btn=Button(root,text="Show Records in the database",command=display)
  display_btn.grid(row=7,column=1)

  delete_btn=Button(root,text="delete record",command=delete)
  delete_btn.grid(row=8,column=1)"""


  conn.commit()


def login():
  rot=Tk()
  conn=sqlite3.connect('acc.db')
  c=conn.cursor()
  rot.title('Login!')
  rot.geometry("400x400")
  lname=Entry(rot,width=30)
  lname.grid(row=0,column=1)
  lpassword=Entry(rot,width=30)
  lpassword.grid(row=1,column=1)
  
  lname_label=Label(rot,text="User Name")
  lname_label.grid(row=0,column=0)
  lpassword_label=Label(rot,text="Password")
  lpassword_label.grid(row=1,column=0)

  def check():
    conn=sqlite3.connect('acc.db')
    c=conn.cursor()
    c.execute("DELETE FROM c")
    o1=0
    c.execute("INSERT INTO c VALUES(:n,:p)",
    {
      'n' : lname.get(),
      'p' : lpassword.get(),
    })
    lname.delete(0,END)
    lpassword.delete(0,END)
    conn.commit()
    c.execute("SELECT * FROM Account")
    h2=len(c.fetchall())
    c.execute("SELECT *,oid FROM Account")
    records1=c.fetchall()
    c.execute("SELECT *,oid FROM c")
    records2=c.fetchall()
    h=0
    for r1 in records1:
      for r2 in records2:
        if(h<h2):
          d1=records1[h]
          d2=records2[0]
          pr1=""
          if(d1[0]==d2[0] and d1[1]==d2[1]):
            o1=1
            pr1+=d2[0]
            break
          h+=1
      
    if(o1==1):
      q1_label=Label(rot,text="Account Access Granted Welcome "+pr1)
      q1_label.grid(row=5,column=0,columnspan=4)
      
    else:
      q2_label=Label(rot,text="Account Access Denied Try Again"+pr1)
      q2_label.grid(row=5,column=0,columnspan=4)
    

  s_btn=Button(rot,text="Check",command=check)
  s_btn.grid(row=3,column=0)
  conn.commit()
  
signup_btn=Button(r,text="Sign Up",command=signup)
signup_btn.grid(row=0,column=0)

login_btn=Button(r,text="Login",command=login)
login_btn.grid(row=1,column=0)

conn.commit()
r.mainloop()

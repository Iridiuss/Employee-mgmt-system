def searchall():
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee"
        mycursor=mydb.cursor()
        mycursor.execute(sql_query)
        empl=mycursor.fetchall()
        if len(empl)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            for emp in empl :
                treeview_display_students.insert(parent='',index='end',values=emp)

def searchno():
    rn= int(entryno.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where empno=%s"
        values=[rn]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        empl=mycursor.fetchone()
        if empl==None:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(empl)

            for row in treeview_display_students.get_children():
                treeview_display_students.delete(row) 
            treeview_display_students.insert(parent='',index='end',values=empl)
def searchname():
    nm=entryname.get()
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where empname like %s"
        values=[nm+"%"]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        emps=mycursor.fetchall()
        if len(emps)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(emps)
            for empl in emps :
                treeview_display_students.insert(parent='',index='end',values=empl)

def searchjob():
    jb=entryjob.get()
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where job like %s"
        values=[jb]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        emps=mycursor.fetchall()
        if len(emps)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(emps)
            for empl in emps :
                treeview_display_students.insert(parent='',index='end',values=empl)

def searchmgr():
    mg=int(entrymgr.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    for row in treeview_display_students.get_children():
                treeview_display_students.delete(row) 
    if mydb== 0:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where mgr=%s"
        values=[mg]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        empl=mycursor.fetchall()
        if len(empl)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(empl)
            for emp in empl :
                treeview_display_students.insert(parent='',index='end',values=emp)

def searchdate():
    hd=entryhiredate.get()
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    for row in treeview_display_students.get_children():
                treeview_display_students.delete(row) 
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where hiredate=%s"
        values=[hd]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        empl=mycursor.fetchall()
        if len(empl)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(empl)
            for emp in empl :
                treeview_display_students.insert(parent='',index='end',values=emp)

def searchsal():
    sl=float(entrysal.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    for row in treeview_display_students.get_children():
                treeview_display_students.delete(row) 
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where sal=%s"
        values=[sl]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        empl=mycursor.fetchall()
        if len(empl)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(empl)
            for emp in empl :
                treeview_display_students.insert(parent='',index='end',values=emp)

def searchcomm():
    cm=entrycom.get()
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    for row in treeview_display_students.get_children():
                treeview_display_students.delete(row) 
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where comm=%s"
        values=[cm]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        empl=mycursor.fetchall()
        if len(empl)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(empl)
            for emp in empl :
                treeview_display_students.insert(parent='',index='end',values=emp)

def searchdn():
    dn=int(entrydeptno.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    for row in treeview_display_students.get_children():
                treeview_display_students.delete(row) 
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query="select*from employee where deptno=%s"
        values=[dn]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        empl=mycursor.fetchall()
        if len(empl)==0:
            print("employee not found")
            labelstatus.configure(text='employee not found')
        else:
            print(empl)
            for emp in empl :
                treeview_display_students.insert(parent='',index='end',values=emp)

def deleteno():
    en= int(entryno.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee where empno= %s'
        values=[en]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        if(mycursor.rowcount>0):
             labelstatus.configure(text='employee' +str(en) +'deleted')
        else:
             labelstatus.configure(text='employee not found')
        mydb.commit()
        mydb.close()

def deletenm():
    nm=entryname.get()
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee where empname= %s'
        values=[nm]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        if(mycursor.rowcount>0):
             labelstatus.configure(text='employee' +'' +nm +''+'deleted')
        else:
             labelstatus.configure(text='employee not found')
        mydb.commit()
        mydb.close()

def deletej():
    jb=entryjob.get()
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee where job= %s'
        values=[jb]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        if(mycursor.rowcount>0):
             labelstatus.configure(text='employee' +'' +jb +''+'deleted')
        else:
             labelstatus.configure(text='employee not found')
        mydb.commit()
        mydb.close()

def deletemgr():
    mg=int(entrymgr.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee where mgr= %s'
        values=[mg]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        if(mycursor.rowcount>0):
             labelstatus.configure(text='employee' +'' +str(mg) +''+'deleted')
        else:
             labelstatus.configure(text='employee not found')
        mydb.commit()
        mydb.close()

def deletehd():
    hd=entryhiredate.get()
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee where hiredate= %s'
        values=[hd]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        if(mycursor.rowcount>0):
             labelstatus.configure(text='employee' +'' +str(hd) +''+'deleted')
        else:
             labelstatus.configure(text='employee not found')
        mydb.commit()
        mydb.close()

def deletesal():
    sl=float(entrysal.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee where sal= %s'
        values=[sl]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        if(mycursor.rowcount>0):
             labelstatus.configure(text='employee' +'' +str(sl) +''+'deleted')
        else:
             labelstatus.configure(text='employee not found')
        mydb.commit()
        mydb.close()
    
def deletedeptno():
    dn=int(entrydeptno.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee where deptno= %s'
        values=[dn]
        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        if(mycursor.rowcount>0):
             labelstatus.configure(text='employee' +'' +str(dn) +''+'deleted')
        else:
             labelstatus.configure(text='employee not found')
        mydb.commit()
        mydb.close()

def deleteall():
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        sql_query= 'delete from employee'
        mycursor=mydb.cursor()
        mycursor.execute(sql_query)
        labelstatus.configure(text='all employee data deleted')
        mydb.commit()
        mydb.close()

def addemployee():
    en= int(entryno.get())
    nm=entryname.get()
    jb=entryjob.get()
    mg=int(entrymgr.get())
    hd=entryhiredate.get()
    sl=float(entrysal.get())
    cm=entrycom.get()
    dn=int(entrydeptno.get())
    mydb = bot.connect(host = 'localhost',user = 'root',password = 'Tiger@123',database = 'gds')
    if mydb== None:
        print("not connected")
    else:
        print("connection successful")
        mycursor=mydb.cursor()
        #inserting data into table
        sql_query= 'insert into employee(empno,empname,job,mgr,hiredate,sal,comm,deptno) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(en,nm,jb,mg,hd,sl,cm,dn)
        mycursor.execute(sql_query,values)
        mydb.commit()
        mydb.close()
        omsg=f'{en},{nm},{jb},{mg},{hd} ,{sl},{cm},{dn} added successfully'
        labelstatus.configure(text=omsg)
import mysql.connector as bot 
import tkinter as tk
from tkinter import ttk
rootwindow= tk.Tk()
rootwindow.geometry('800x600')
rootwindow.configure(background='cyan')
frame1=tk.Frame(
    master=rootwindow,padx=10,pady=10
)
frame2=tk.Frame(
    master=rootwindow,padx=10,pady=10
)
frame3=tk.Frame(
    master=rootwindow,padx=10,pady=10
)
frame1.pack()
frame2.pack()
frame3.pack()
heading=tk.Label (
    master=frame1,
    text="Employee management system",
    font=('ariel',10,'bold'),
    background='pink'
)
frameinputdetails=tk.LabelFrame (
    master=frame2,
    text='enter employee details',
    background='cyan'
)
framestatus=tk.Frame(
    master=rootwindow,padx=10,pady=10
)
treeview_display_students = ttk.Treeview(
            master = rootwindow,
            columns = (1,2,3,4,5,6,7,8),
            show = 'headings',
            height = 5)
treeview_display_students.heading(1,text='empnp')
treeview_display_students.heading(2,text='emp name')
treeview_display_students.heading(3,text='job')
treeview_display_students.heading(4,text='mgr')
treeview_display_students.heading(5,text='hiredate')
treeview_display_students.heading(6,text='sal')
treeview_display_students.heading(7,text='comm')
treeview_display_students.heading(8,text='deptno')

labelno=tk.Label(
    master=frameinputdetails,
    text='enter empno',
    background='cyan'
)
labelname=tk.Label(
    master=frameinputdetails,
    text='enter emp name',
    background='cyan'
)
labeljob=tk.Label(
    master=frameinputdetails,
    text='enter job',
    background='cyan'
)
labelmgr=tk.Label(
    master=frameinputdetails,
    text='enter mgr',
    background='cyan'
)
labelhiredate=tk.Label(
    master=frameinputdetails,
    text='enter hiredate',
    background='cyan'
)
labelsal=tk.Label(
    master=frameinputdetails,
    text='enter salary',
    background='cyan'
)
labelcom=tk.Label(
    master=frameinputdetails,
    text='enter comm',
    background='cyan'
)
labeldeptno=tk.Label(
    master=frameinputdetails,
    text='enter deptno',
    background='cyan'
)
entryno=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
entryname=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
entryjob=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
entrymgr=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
entryhiredate=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
entrysal=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
entrycom=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
entrydeptno=tk.Entry(
    master=frameinputdetails,
    background='pink'
)
buttonaddemployee=tk.Button(
    master=frameinputdetails,
    text='add employee',
    command=addemployee
)
buttonsearch=tk.Button(
    master=frameinputdetails,
    text='search empno',
    command=searchno
)
buttonsearchall=tk.Button(
    master=frameinputdetails,
    text='search all',
    command=searchall
)
buttonsearchn=tk.Button(
    master=frameinputdetails,
    text='search name',
    command=searchname
)
buttonsearchj=tk.Button(
    master=frameinputdetails,
    text='search job',
    command=searchjob
)
buttonsearchm=tk.Button(
    master=frameinputdetails,
    text='search manager',
    command=searchmgr
)
buttonsearchd=tk.Button(
    master=frameinputdetails,
    text='search hiredate',
    command=searchdate
)
buttonsearchs=tk.Button(
    master=frameinputdetails,
    text='search salary',
    command=searchsal
)
buttonsearchc=tk.Button(
    master=frameinputdetails,
    text='search comm',
    command=searchcomm
)
buttonsearchdn=tk.Button(
    master=frameinputdetails,
    text='search deptno',
    command=searchdn
)
buttondeleteno=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=deleteno,
    background='red'
)
buttondeletenm=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=deletenm,
    background='red'
)
buttondeletej=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=deletej,
    background='red'
)
buttondeletemgr=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=deletemgr,
    background='red'
)
buttondeletehd=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=deletehd,
    background='red'
)
buttondeletesal=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=deletesal,
    background='red'
)
buttondeletecomm=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=searchdn,
    background='red'
)
buttondeletedn=tk.Button(
    master=frameinputdetails,
    text='delete',
    command=deletedeptno,
    background='red'
)
buttondeleteall=tk.Button(
    master=frameinputdetails,
    text='delete all',
    command=deleteall,
    background='red'
)
labelstatus= tk.Label(
    master=framestatus,
    text='',
    background='pink'
)
heading.pack()
frameinputdetails.pack(fill='both',expand='yes',padx=10,pady=10)
framestatus.pack()
labelstatus.pack()
labelno.grid(row=0,column=0,padx=10,pady=10)
labelname.grid(row=1,column=0,padx=10,pady=10)
labeljob.grid(row=2,column=0,padx=10,pady=10)
labelmgr.grid(row=3,column=0,padx=10,pady=10)
labelhiredate.grid(row=4,column=0,padx=10,pady=10)
labelsal.grid(row=5,column=0,padx=10,pady=10)
labelcom.grid(row=6,column=0,padx=10,pady=10)
labeldeptno.grid(row=7,column=0,padx=10,pady=10)

entryno.grid(row=0,column=1,padx=10,pady=10)
entryname.grid(row=1,column=1,padx=10,pady=10)
entryjob.grid(row=2,column=1,padx=10,pady=10)
entrymgr.grid(row=3,column=1,padx=10,pady=10)
entryhiredate.grid(row=4,column=1,padx=10,pady=10)
entrysal.grid(row=5,column=1,padx=10,pady=10)
entrycom.grid(row=6,column=1,padx=10,pady=10)
entrydeptno.grid(row=7,column=1,padx=10,pady=10)
buttonaddemployee.grid(row=8,column=2,padx=10,pady=10)
buttonsearchall.grid(row=8,column=3,padx=10,pady=10)
buttondeleteall.grid(row=8,column=1,padx=10,pady=10)
buttonsearch.grid(row=0,column=2,padx=10,pady=10)
buttonsearchn.grid(row=1,column=2,padx=10,pady=10)
buttonsearchj.grid(row=2,column=2,padx=10,pady=10)
buttonsearchm.grid(row=3,column=2,padx=10,pady=10)
buttonsearchd.grid(row=4,column=2,padx=10,pady=10)
buttonsearchs.grid(row=5,column=2,padx=10,pady=10)
buttonsearchc.grid(row=6,column=2,padx=10,pady=10)
buttonsearchdn.grid(row=7,column=2,padx=10,pady=10)

buttondeleteno.grid(row=0,column=3,padx=10,pady=10)
buttondeletenm.grid(row=1,column=3,padx=10,pady=10)
buttondeletej.grid(row=2,column=3,padx=10,pady=10)
buttondeletemgr.grid(row=3,column=3,padx=10,pady=10)
buttondeletehd.grid(row=4,column=3,padx=10,pady=10)
buttondeletesal.grid(row=5,column=3,padx=10,pady=10)
buttondeletecomm.grid(row=6,column=3,padx=10,pady=10)
buttondeletedn.grid(row=7,column=3,padx=10,pady=10)

treeview_display_students.pack(fill='both',expand='yes',padx=10,pady=10)
tk.mainloop()
import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import backend
from s1 import student
from s1 import admin

class Login:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window, bg='Blue', width=800, height=700)

    def loginfn(self):
        self.clear_frame()
        self.label = Label(self.frame, text='Library Management System', bg='Orange', font=('Georgia', 36, 'bold'))
        self.buttonadmin = Button(self.frame, text='Admin', bg='Orange', font=('Georgia', 36, 'bold'), command=self.adminlogin)
        self.buttonstudent = Button(self.frame, text='Student', bg='Orange', font=('Georgia', 36, 'bold'), command=self.studentlogin)

        self.label.place(x=45, y=40, width=700, height=80)
        self.buttonadmin.place(x=105, y=200, width=250, height=50)
        self.buttonstudent.place(x=450, y=200, width=250, height=50)
        self.frame.pack()

    def studentlogin(self):
        self.clear_frame()

        self.label = Label(self.frame, text='Log In', bg='Orange', font=('Georgia', 36, 'bold'))
        self.label1 = Label(self.frame, text='Student', bg='Orange', font=('Georgia', 36, 'bold'))

        self.name = Label(self.frame, text='Enter User_Name: ', bg='Orange', font=('Arial', 18, 'bold'))
        self.namee_text = StringVar()
        self.namee = Entry(self.frame, textvariable=self.namee_text, fg='gray', width=25, font=('Arial', 16, 'bold'))

        self.password1 = Label(self.frame, text='Enter Password : ', bg='Orange', fg='Green', font=('Arial', 18, 'bold'))
        self.password1e_text = StringVar()
        self.password1e = Entry(self.frame, textvariable=self.password1e_text, bg='White', fg='gray', width=25, font=('Arial', 16, 'bold'), show='*')

        self.buttonlogin = Button(self.frame, text='LOG IN', bg='gray', fg='gray12', font=('Georgia', 18, 'bold'), cursor='hand2',command=self.login_student)
        self.buttonback = Button(self.frame, text='BACK', bg='gray', fg='gray12', font=('Georgia', 14, 'bold'), cursor='hand2', command=self.loginfn)

        self.buttonregister = Button(self.frame, text='REGISTER', bg='gray', fg='gray12', font=('Georgia', 18, 'bold'), cursor='hand2', command=self.register)

        self.label.place(x=40, y=40, width=200, height=80)
        self.label1.place(x=230, y=40, width=200, height=80)
        self.name.place(x=40, y=140, width=240, height=60)
        self.namee.place(x=380, y=150, width=200, height=30)
        self.password1.place(x=40, y=220, width=240, height=30)
        self.password1e.place(x=380, y=215, width=200, height=30)
        self.buttonlogin.place(x=40, y=300, width=140, height=50)
        self.buttonregister.place(x=250, y=300, width=140, height=50)
        self.buttonback.place(x=420, y=300, width=140, height=40)
       
        self.frame.pack()
    def register(self):
        self.clear_frame()
        self.window.geometry('800x700')  
        self.window.configure(bg='Blue')  


        self.labelr = Label(self.frame, text='Register', bg='Orange', font=('Georgia', 32, 'bold'))
        self.namer = Label(self.frame, text='Name : ', bg='Orange', font=('Arial', 14, 'bold'))
        self.namere_text = StringVar()
        self.namere = Entry(self.frame, textvariable=self.namere_text, fg='gray')

        self.idr = Label(self.frame, text='Roll No. : ', bg='Orange', font=('Arial', 14, 'bold'))
        self.rollno_text = StringVar()
        self.idre = Entry(self.frame, textvariable=self.rollno_text, fg='gray', width=25, font=('Arial', 12, 'bold'))

        self.emailr = Label(self.frame, text='Email ID : ', bg='Orange', font=('Arial', 14, 'bold'))
        self.emailr_text = StringVar()
        self.emailre = Entry(self.frame, textvariable=self.emailr_text, fg='gray', width=25, font=('Arial', 12, 'bold'))

        self.phoner = Label(self.frame, text='Phone Number : ', bg='Orange', font=('Arial', 14, 'bold'))
        self.phoner_text = StringVar()
        self.phonere = Entry(self.frame, textvariable=self.phoner_text, fg='gray', width=25, font=('Arial', 12, 'bold'))


        self.passwordr1 = Label(self.frame, text='Create Password : ', bg='Orange', fg='Green', font=('Arial', 14, 'bold'))
        self.passwordr1e_text = StringVar()
        self.passwordr1e = Entry(self.frame, textvariable=self.passwordr1e_text, bg='White', fg='gray', width=25, font=('Arial', 12, 'bold'), show='*')

        self.reenter_password = Label(self.frame, text='Re-enter Password : ', bg='Orange', fg='Green', font=('Arial', 14, 'bold'))
        self.reenter_password_text = StringVar()
        self.reenter_password_entry = Entry(self.frame, textvariable=self.reenter_password_text, bg='White', fg='gray', width=25, font=('Arial', 12, 'bold'), show='*')


        self.buttonr = Button(self.frame, text='Register', bg='gray', fg='gray12', font=('Georgia', 14, 'bold'), cursor='hand2', command=self.create)
        self.aadhar = Label(self.frame, text='AADHAAR', bg='orange', font=('Arial', 14, 'bold'))
        self.aadhar1 = Entry(self.frame, bg='White', fg='gray', width=25, font=('Arial', 12, 'bold'))
        self.buttonback = Button(self.frame, text='BACK', bg='gray', fg='gray12', font=('Georgia', 14, 'bold'), cursor='hand2', command=self.loginfn)


        self.labelr.place(x=40, y=10, width=200, height=80)
        self.namer.place(x=40, y=100, width=240, height=60)
        self.namere.place(x=300, y=100, width=200, height=30)
        self.idr.place(x=40, y=150, width=240, height=60)
        self.idre.place(x=300, y=150, width=200, height=30)
        self.emailr.place(x=40, y=200, width=240, height=30)
        self.emailre.place(x=300, y=200, width=200, height=30)
        self.phoner.place(x=40, y=250, width=240, height=30)
        self.phonere.place(x=300, y=250, width=200, height=30)
        self.passwordr1.place(x=40, y=350, width=240, height=30)
        self.passwordr1e.place(x=300, y=350, width=200, height=30)
        self.reenter_password.place(x=40, y=400, width=240, height=30)
        self.reenter_password_entry.place(x=300, y=400, width=200, height=30)
        self.buttonr.place(x=160, y=450, width=140, height=40)
        self.aadhar.place(x=40, y=300, width=240, height=30)
        self.aadhar1.place(x=300, y=300, width=200, height=30)
        self.buttonback.place(x=320, y=450, width=140, height=40)
        self.frame.pack()

    def create(self):
        if len(self.namere.get()) == 0:
            MessageBox.showinfo('Error', 'Name field is empty')
        elif len(self.idre.get()) == 0:
            MessageBox.showinfo('Error', 'ID field is empty')
        elif len(self.passwordr1e.get()) == 0:
            MessageBox.showinfo('Error', 'PASSWORD field is empty')
        else:
            self.insert(self.idre.get(), self.namere.get(), self.passwordr1e.get(),self.aadhar1.get(),self.emailre.get(),self.phonere.get())
  
    def insert(self, rollno, name, password,email_id,aadhar,phoneno):
        try:
            conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="studentlogin",auth_plugin="mysql_native_password")
            cur = conn.cursor()
            cur.execute('INSERT INTO user VALUES(%s, %s, %s,%s,%s,%s)', (rollno, name, password,email_id,phoneno,aadhar))
            conn.commit()
            MessageBox.showinfo('Success', 'Record inserted successfully')
        except mysql.Error as error:
            MessageBox.showerror('Error', f'Error: {error}')
        finally:
            if conn.is_connected():
                conn.close()

    def login_student(self):
        
        if len(self.namee.get()) ==0:
            MessageBox.showinfo("ERROR", "Mendatory Field is empty")
        elif  len(self.password1e.get()) == 0:
            MessageBox.showinfo("ERROR", "Mendatory Field is empty")
        else:
            self.checks(self.namee_text.get(),self.password1e_text.get())
              
              

    def checks(self, name, password):
        try:
            conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="studentlogin", auth_plugin="mysql_native_password")
            cur = conn.cursor()
            cur.execute('SELECT * FROM user WHERE name = %s AND password = %s', (name, password))
            if cur.fetchone():
                MessageBox.showinfo('Success', 'Login successful')
                self.window.destroy() 

                first_window = Tk()
                first_window.title('Student_User')
                first_window.geometry('700x400')
                obj = student(first_window)
                first_window.mainloop()
         
            else:
                MessageBox.showinfo('Error', 'Invalid credentials for STUDENT LOGIN')
        except mysql.Error as error:
            MessageBox.showerror('Error', f'Error: {error}')
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()
    

    









# admin part











    def admininsert(self, lastname, name, password,email_id,aadhar,phoneno):
        try:
            conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="adminlogin",auth_plugin="mysql_native_password")
            cur = conn.cursor()
            cur.execute('INSERT INTO adminuser VALUES(%s, %s, %s,%s,%s,%s)', (lastname, name, password,email_id,phoneno,aadhar))
            conn.commit()
            MessageBox.showinfo('Success', 'Record inserted successfully')
        except mysql.Error as error:
            MessageBox.showerror('Error', f'Error: {error}')
        finally:
            if conn.is_connected():
                conn.close()

    def adminlogin(self):
        self.clear_frame()

        self.label = Label(self.frame, text='Log In', bg='Orange', font=('Georgia', 36, 'bold'))
        self.label1 = Label(self.frame, text='Admin', bg='Orange', font=('Georgia', 36, 'bold'))

        self.name = Label(self.frame, text='Enter User_Name: ', bg='Orange', font=('Arial', 18, 'bold'))
        self.namee_text = StringVar()
        self.namee = Entry(self.frame, textvariable=self.namee_text, fg='gray', width=25, font=('Arial', 16, 'bold'))

        self.password1 = Label(self.frame, text='Enter Password : ', bg='Orange', fg='Green', font=('Arial', 18, 'bold'))
        self.password1e_text = StringVar()
        self.password1e = Entry(self.frame, textvariable=self.password1e_text, bg='White', fg='gray', width=25, font=('Arial', 16, 'bold'), show='*')

        self.buttonlogin = Button(self.frame, text='LOG IN', bg='gray', fg='gray12', font=('Georgia', 18, 'bold'), cursor='hand2',command=self.login_admin)
        self.buttonregister = Button(self.frame, text='REGISTER', bg='gray', fg='gray12', font=('Georgia', 18, 'bold'), cursor='hand2', command=self.adminregister)
        self.buttonback = Button(self.frame, text='BACK', bg='gray', fg='gray12', font=('Georgia', 14, 'bold'), cursor='hand2', command=self.loginfn)

        self.label.place(x=40, y=40, width=200, height=80)
        self.label1.place(x=230, y=40, width=200, height=80)
        self.name.place(x=40, y=140, width=240, height=60)
        self.namee.place(x=380, y=150, width=200, height=30)
        self.password1.place(x=40, y=220, width=240, height=30)
        self.password1e.place(x=380, y=215, width=200, height=30)
        self.buttonlogin.place(x=40, y=300, width=140, height=50)
        self.buttonregister.place(x=250, y=300, width=140, height=50)
        self.buttonback.place(x=420, y=300, width=140, height=40)
        self.frame.pack()

    


    def adminregister(self):
            self.clear_frame()
            self.window.geometry('800x700')  
            self.window.configure(bg='Blue')  


            self.labelr = Label(self.frame, text='Register', bg='Orange', font=('Georgia', 32, 'bold'))
            self.namer = Label(self.frame, text=' First Name : ', bg='Orange', font=('Arial', 14, 'bold'))
            self.namere_text = StringVar()
            self.namere = Entry(self.frame, textvariable=self.namere_text, fg='gray')

            self.last = Label(self.frame, text='Last Name. : ', bg='Orange', font=('Arial', 14, 'bold'))
            self.lastname_text = StringVar()
            self.lastr= Entry(self.frame, textvariable=self.lastname_text, fg='gray', width=25, font=('Arial', 12, 'bold'))

            self.emailr = Label(self.frame, text='Email ID : ', bg='Orange', font=('Arial', 14, 'bold'))
            self.emailr_text = StringVar()
            self.emailre = Entry(self.frame, textvariable=self.emailr_text, fg='gray', width=25, font=('Arial', 12, 'bold'))

            self.phoner = Label(self.frame, text='Phone Number : ', bg='Orange', font=('Arial', 14, 'bold'))
            self.phoner_text = StringVar()
            self.phonere = Entry(self.frame, textvariable=self.phoner_text, fg='gray', width=25, font=('Arial', 12, 'bold'))


            self.passwordr1 = Label(self.frame, text='Create Password : ', bg='Orange', fg='Green', font=('Arial', 14, 'bold'))
            self.passwordr1e_text = StringVar()
            self.passwordr1e = Entry(self.frame, textvariable=self.passwordr1e_text, bg='White', fg='gray', width=25, font=('Arial', 12, 'bold'), show='*')

            self.reenter_password = Label(self.frame, text='Re-enter Password : ', bg='Orange', fg='Green', font=('Arial', 14, 'bold'))
            self.reenter_password_text = StringVar()
            self.reenter_password_entry = Entry(self.frame, textvariable=self.reenter_password_text, bg='White', fg='gray', width=25, font=('Arial', 12, 'bold'), show='*')


            self.buttonr = Button(self.frame, text='Register', bg='gray', fg='gray12', font=('Georgia', 14, 'bold'), cursor='hand2', command=self.admincreate)
            self.aadhar = Label(self.frame, text='AADHAAR', bg='orange', font=('Arial', 14, 'bold'))
            self.aadhar1 = Entry(self.frame, bg='White', fg='gray', width=25, font=('Arial', 12, 'bold'))
            self.buttonback = Button(self.frame, text='BACK', bg='gray', fg='gray12', font=('Georgia', 14, 'bold'), cursor='hand2', command=self.loginfn)


            self.labelr.place(x=40, y=10, width=200, height=80)
            self.namer.place(x=40, y=100, width=240, height=60)
            self.namere.place(x=300, y=100, width=200, height=30)
            self.last.place(x=40, y=150, width=240, height=60)
            self.lastr.place(x=300, y=150, width=200, height=30)
            self.emailr.place(x=40, y=200, width=240, height=30)
            self.emailre.place(x=300, y=200, width=200, height=30)
            self.phoner.place(x=40, y=250, width=240, height=30)
            self.phonere.place(x=300, y=250, width=200, height=30)
            self.passwordr1.place(x=40, y=350, width=240, height=30)
            self.passwordr1e.place(x=300, y=350, width=200, height=30)
            self.reenter_password.place(x=40, y=400, width=240, height=30)
            self.reenter_password_entry.place(x=300, y=400, width=200, height=30)
            self.buttonr.place(x=160, y=450, width=140, height=40)
            self.aadhar.place(x=40, y=300, width=240, height=30)
            self.aadhar1.place(x=300, y=300, width=200, height=30)
            self.buttonback.place(x=320, y=450, width=140, height=40)
            self.frame.pack()    

    def admincreate(self):
        if len(self.namere.get()) == 0:
            MessageBox.showinfo('Error', 'Name field is empty')
        elif len(self.lastr.get()) == 0:
            MessageBox.showinfo('Error', 'ID field is empty')
        elif len(self.passwordr1e.get()) == 0:
            MessageBox.showinfo('Error', 'PASSWORD field is empty')
        else:
            self.admininsert(self.lastr.get(), self.namere.get(), self.passwordr1e.get(),self.aadhar1.get(),self.emailre.get(),self.phonere.get())

    

    def login_admin(self):
        if len(self.namee.get()) ==0:
            MessageBox.showinfo("ERROR", "Mendatory Field is empty")
        elif  len(self.password1e.get()) == 0:
            MessageBox.showinfo("ERROR", "Mendatory Field is empty")
        else:
            self.check(self.namee_text.get(),self.password1e_text.get())
           

            



    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


    
    def check(self, name, password):
        try:
            conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="adminlogin", auth_plugin="mysql_native_password")
            cur = conn.cursor()
            cur.execute('SELECT * FROM adminuser WHERE name = %s AND password = %s', (name, password))
            if cur.fetchone():
                MessageBox.showinfo('Success', 'Login successful')

                self.window.destroy() 
                second_window = Tk()
                second_window.title('Admin_User')
                second_window.geometry('700x450')
                obj = admin(second_window)
                second_window.mainloop()
            else:
                MessageBox.showinfo('Error', 'Invalid credentials for ADMIN LOGIN')
        except mysql.Error as error:
            MessageBox.showerror('Error', f'Error: {error}')
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    # con.commit()
    # con.close()

                   


window = Tk()
window.title('Login')
window.geometry('700x400')
obj = Login(window)
obj.loginfn()
window.mainloop()

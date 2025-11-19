# USING PACK()

import tkinter as tk
from tkinter import messagebox
def say_hello():
    print('HELLLO TO TKINTER')
    
def check_box():
    print(var.get())
    if var.get() == 1:
        print('thank you for accepting....')
    else:
        print('sorry! you are not allowed....')
        
def radio_button():
    print(choice.get())
    print('radio button created....')
    
def show_msg():
    messagebox.showinfo("Info","This is an info message")
    messagebox.showwarning("Warning","This is a warning!")
    messagebox.showerror("Error","Oops! Something went wrong..")
    
def frame_button():
    print('Frame button is Clicked')
    
root = tk.Tk()
# title
root.title('The tkinter GUI')

# size
root.geometry('500x500')

# text
tk.Label(root,text = 'Hello Tkinter!1',font=('Arial',16)).pack(pady=20)
tk.Label(root,text='Hello Tkinter!2',font=('Arial',16)).pack(pady=20)

# butoon
tk.Button(root,text = "click me",command = say_hello).pack(pady=10)
tk.Button(root,text="CLICK",command=show_msg).pack(pady=10)

# entry input box
tk.Entry(root).pack(pady=10)
tk.Entry(root).pack(pady=10)

# password feild type
tk.Entry(root,show='*').pack()


# text area type
# tk.Text().pack()

# check box
var = tk.IntVar()
tk.Checkbutton(root,text='i agree',variable=var,command=check_box).pack(pady=10)

# radio button
choice = tk.StringVar()
tk.Radiobutton(root,text=" OPTION A",variable=choice,value='A',command=radio_button).pack(pady=10)
tk.Radiobutton(root,text=" OPTION B",variable=choice,value='B',command=radio_button).pack(pady=10)

# list
listbox = tk.Listbox(root)
listbox.insert(1,'python')
listbox.insert(2,'java')
listbox.insert(3,'C++')
listbox.pack()


frame = tk.Frame(root,bd=3,height=60,width=100,relief='solid')
frame.pack()

tk.Label(frame,text='Inside Frame').grid(row=0,column=0)
tk.Button(frame,text='click',command=frame_button).grid(row=0,column=1)
tk.Label(root,text="hello").place(x=50,y=100)
root.mainloop()

# USING GRID()

import tkinter as tk
from tkinter import messagebox
def say_hello():
    print('HELLLO TO TKINTER')
    
def check_box():
    print(var.get())
    if var.get() == 1:
        print('thank you for accepting....')
    else:
        print('sorry! you are not allowed....')
        
def radio_button():
    print(choice.get())
    print('radio button created....')
    
def show_msg():
    messagebox.showinfo("Info","This is an info message")
    messagebox.showwarning("Warning","This is a warning!")
    messagebox.showerror("Error","Oops! Something went wrong..")
    
def frame_button():
    print('Frame button is Clicked....')
    
root = tk.Tk()
# title
root.title('The tkinter GUI')

# size
root.geometry('500x500')

# text
tk.Label(root,text = 'Hello Tkinter!1',font=('Arial',16)).grid(row=0,column=0)
tk.Label(root,text='Hello Tkinter!2',font=('Arial',16)).grid(row=0,column=1)

# butoon
tk.Button(root,text = "click me",command = say_hello).grid(row=1,column=0)
tk.Button(root,text="CLICK",command=show_msg).grid(row=1,column=1)

# entry input box
tk.Entry(root).grid(row=2,column=0)
tk.Entry(root).grid(row=2,column=1)

# password feild type
tk.Entry(root,show='*').grid(row=3,column=0)


# text area type
# tk.Text().pack()

# check box
var = tk.IntVar()
tk.Checkbutton(root,text='i agree',variable=var,command=check_box).grid(row=3,column=1)

# radio button
choice = tk.StringVar()
tk.Radiobutton(root,text=" OPTION A",variable=choice,value='A',command=radio_button).grid(row=4,column=0)
tk.Radiobutton(root,text=" OPTION B",variable=choice,value='B',command=radio_button).grid(row=4,column=1)

# list
listbox = tk.Listbox(root)
listbox.insert(1,'python')
listbox.insert(2,'java')
listbox.insert(3,'C++')
listbox.grid(row=5,column=0)

frame = tk.Frame(root,bd=5,height=50,width=90,relief='solid')
frame.grid(row=5,column=1)
tk.Label(frame,text="inside frame").pack(pady=10)
tk.Button(frame,text="Click",command=frame_button).pack(pady=10)


root.mainloop()



# TASK
# Create a tkinter module which can take username, password from user's GUI and check in the database if such username and passwords exists.

import tkinter as tk
from tkinter import messagebox
import mysql.connector
def check_login():
    username = entry_username.get()
    password = entry_password.get()
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Kaveri@123",
            database = "56r"
        )
        cursor = conn.cursor()
        
        query = "select * from users where username = %s and password = %s"
        cursor.execute(query,(username,password))
        result = cursor.fetchone()
        
        if result:
            messagebox.showinfo("Success","Logi Successfl!")
        else:
            messagebox.showerror("Failed","Invalid username or password!,Check it Once")
        
        conn.close()
        
    except mysql.connector.Error as err:
        messagebox.showerror("ERROR",f"Database error:{err}")  
        
    
    
root = tk.Tk()

root.title('tkinter TASK')
root.geometry('300x300')

tk.Label(root,text='Username',font=('Arial',16)).grid(row=0,column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0,column=1)

tk.Label(root,text='Password',font=('Arial',16)).grid(row=1,column=0)
entry_password = tk.Entry(root,show="*")
entry_password.grid(row=1,column=1)

tk.Button(root,text="Login",command=check_login).grid(row=2,column=0,columnspan=2,pady=20)


root.mainloop()




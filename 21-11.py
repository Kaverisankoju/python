import tkinter as tk
from tkinter import filedialog,messagebox
import csv
import mysql.connector

try:
  
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',   #sql password
        database = '56r',
        autocommit = False
    )
    print(conn.is_connected())
    cursor = conn.cursor()
    
except mysql.connector.Error as err:
    messagebox.showerror("DB Error",f"Database Connection Failed:\n{err}")
    exit()
    

   
def csv_file_upload_function():
    try:
        
        filename = filedialog.askopenfilename(filetypes=[('CSV FILES','*.csv')])
        if not filename:
            return
        
      
        with open(filename,'r') as f:
            data = csv.reader(f)
            print(next(data)) 
            
         
            for row in data:
                cursor.execute('''INSERT INTO STUDENT1(NAME,AGE,GRADE) VALUES (%s,%s,%s)''',(row))
            conn.commit()
            messagebox.showinfo("success","Data is inserted to Database..")    
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error",f"CSV Upload Failed:\n{e}")
        

      
def show_grid():
    try:
        grid.config(state=tk.NORMAL)
        grid.delete('1.0',tk.END)
        
      
        cursor.execute('SELECT*FROM STUDENT1')
        
       
        for row in cursor.fetchall():
            grid.insert(tk.END,f'id: {row[0]},name: {row[1]},age: {row[2]},grade: {row[3]}\n') 
        grid.config(state=tk.DISABLED) 
    except Exception as e:
        messagebox.showerror("Error",f"Failed to load records:\n{e}")
 
def add_record():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    
 
    if not(name and age and grade):
        messagebox.showwarning("Warning","All fields required!")
        return
    try:
        
        cursor.execute('''INSERT INTO STUDENT1(NAME,AGE,GRADE) VALUES (%s,%s,%s)''',(name,age,grade))
        conn.commit()
        messagebox.showinfo('INFO','Record added')
        show_grid()
        
    except Exception as e:
        conn.rollback()
        messagebox.showerror('Error',f"Add Record Failed:\n{e}")
        
        
      
def edit_record():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    if not(id and name and age and grade):
        messagebox.showwarning("Warning","All fields required!")
        return
    try:
        
       
        cursor.execute('''UPDATE STUDENT1 SET NAME= %s, AGE = %s, GRADE = %s WHERE ID = %s ''',(name,age,grade,id))
        conn.commit()
        
        if cursor.rowcount == 0:
             messagebox.showwarning('Warning','ID not found!')
        else:
            messagebox.showinfo("Success","Record Updated!")
        show_grid()
    except Exception as e:
        conn.rollback()
        messagebox.showerror('Error', f'Update Failed:\n{e}')
        
 

def delete_record():
    id = id_entry.get()
    if not id:
        messagebox.showwarning("Warning","ID required!")
        return
    try:
    
        cursor.execute('''DELETE FROM STUDENT1 WHERE ID = %s''',(id,))   
        conn.commit()
        
        if cursor.rowcount == 0:
            messagebox.showwarning('Warning','ID not found!')
        else:
            messagebox.showinfo("Success","Record Deleted!")
            
        show_grid()
        
    except Exception as e:
        conn.rollback()
        messagebox.showerror('Error',f'Delete Failed:\n{e}')

            
root = tk.Tk()
root.geometry("500x500")


tk.Button(root,text="Upload CSV",command=csv_file_upload_function).pack()


grid = tk.Text(root,height=15,width=60)
grid.pack(pady=10)


input_frame = tk.Frame(root)
input_frame.pack(pady=10)


id_label = tk.Label(input_frame,text="ID").grid(row=0,column=0)
id_entry = tk.Entry(input_frame, width=5) 
id_entry.grid(row=0,column=1,padx=5)


name_label = tk.Label(input_frame,text="NAME").grid(row=0,column=2)
name_entry = tk.Entry(input_frame, width=10) 
name_entry.grid(row=0,column=3,padx=5)



age_label = tk.Label(input_frame,text="AGE").grid(row=0,column=4)
age_entry = tk.Entry(input_frame, width=5) 
age_entry.grid(row=0,column=5,padx=5)



grade_label = tk.Label(input_frame,text="GRADE").grid(row=0,column=6)
grade_entry = tk.Entry(input_frame, width=5) 
grade_entry.grid(row=0,column=7,padx=5)


tk.Button(input_frame,text="ADD",command=add_record).grid(row=1,column=2,padx=5)
tk.Button(input_frame,text="EDIT",command=edit_record).grid(row=1,column=3,padx=5)
tk.Button(input_frame,text="DELETE",command=delete_record).grid(row=1,column=4,padx=5)


show_grid()
root.mainloop()

import tkinter
import tkinter as tk
from tkinter import StringVar, Frame, messagebox, ttk

#creation of window
main_window = tk.Tk()
main_window.geometry('360x300')
main_window.title('Employee Record System')

#employee record
employee_record = []
department_options = [ "Human Resources",
    "Finance",
    "Engineering",
    "Marketing",
    "Sales",
    "Information Technology",
    "Customer Service"
]
#global variable
employeeName = StringVar()
department = StringVar()
employment_status = tk.BooleanVar()
#employment_status.set("Part-Time") #default value


#global expressions and functions
def add_employee():
    global employee_record
    global department
    name = employeeName.get()
    department = department_dropdown.get()
    if employment_status.get():
        status = 'Full Time'
    else:
        status = 'Part Time'

    if name == '' or department == '' or status == '':
        messagebox.showerror('Error', 'Please fill in all fields')
        return
    else:
        new_employee = f"Employee: {name}, {department}, {status}"
        employee_record.append((name, department, status))
        list_box.insert(tk.END, new_employee)


def quit_btn():
    main_window.destroy()

def update_showlist():
    global employee_record
    employee_record = employee_record

def edit_employee():
    global employee_record
    global department
    selected_employee = list_box.curselection()
    if not selected_employee:
        messagebox.showerror('Error', 'Please select an employee')
        return

    index = selected_employee[0]
    name = employeeName.get()
    department = department_dropdown.get()
    if employment_status.get():
        status = 'Full Time'
    else:
        status = 'Part Time'

    if name == '' or department == '':
        messagebox.showerror('Error', 'Please fill in all fields')
    else:
        employee_record[index] = (name, department, status)
        updated_employee_record = f"Employee: {name}, {department}, {status}"
        list_box.delete(index)
        list_box.insert(index, updated_employee_record)

def clear_box(): # i'm thinking there have to be a way to just clear up the box.
    employeeName.set("")
    department.set("")
    employment_status.set(False)


#label of name, department, and employeeStatus
name_label = tk.Label(main_window, text='Name', fg='black', bg='#fff')
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(main_window, textvariable=employeeName)
name_entry.grid(row=0, column=1, padx=10, pady=5)

#department
department_label = tk.Label(main_window, text='Department', fg='black', bg='#fff')
department_label.grid(row=1, column=0, padx=10, pady=5)
department_dropdown = ttk.Combobox(main_window, values=department_options, width=15)
department_dropdown.grid(row=1, column=1, padx=10, pady=5)

#employee status
status_label = tk.Label(main_window, text='Employee Status', fg='black', bg='#fff')
status_label.grid(row=2, column=0, padx=10, pady=5)
full_time_check = tk.Checkbutton(main_window, text= "Full Time | If Unchecked: Part-Time", variable=employment_status)
full_time_check.grid(row=2, column=1, padx=10, pady=5)

# add employee and edit employee btn

add_btn = tk.Button(main_window, text="Add Employee", width=10, height=1, bd=1, bg="#eee", cursor= 'hand2', command=add_employee)
add_btn.grid(row=3, column=0, padx=10, pady=5)

edit_btn = tk.Button(main_window, text="Edit Employee", width=10, height=1, bd=1, bg="#eee", cursor= 'hand2', command=edit_employee)
edit_btn.grid(row=3, column=3, padx=10, pady=5)
quit_but = tk.Button(main_window, text="QUIT", width=10, height=1, bd=1, bg="#eee", cursor= 'hand2', command=quit_btn)
quit_but.grid(row=5, column=1, padx=10, pady=5)

#list box
list_frame = tk.Frame(main_window)
list_frame.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

# Scrollbar
list_scroll = tk.Scrollbar(list_frame, orient=tk.VERTICAL)

# Listbox with scrollbar
list_box = tk.Listbox(list_frame, width=50, height=10, yscrollcommand=list_scroll.set)
list_box.pack(side=tk.LEFT, fill=tk.BOTH)

list_scroll.config(command=list_box.yview)
list_scroll.pack(side=tk.RIGHT, fill=tk.Y)




main_window.mainloop()
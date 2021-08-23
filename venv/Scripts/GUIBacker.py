from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox



# create window
window=Tk()
window.title("GUIBancker")
window.grid()
window.geometry('800x800')

# create  name label and entry
name_label=Label(window,text="Имя",font=("Arial",25))
name_label.grid(column=0,row=0)

name_text=StringVar()
name_entry=Entry(window,textvariable=name_text)
name_entry.grid(column=1,row=0)  # this method makes entry visible and add this on window in first column and 0 row

# create surname label and entry

#  create surname label

surname_label=Label(window,text="Фамилия",font=("Arial",25))
surname_label.grid(column=0,row=1)

# create surname entry

surname_text=StringVar()
surname_entry=Entry(textvariable=surname_text)
surname_entry.grid(column=1,row=1)

#  ceate patronic label

patronic_label=Label(window,text="Отчетсво",font=("Arial",25))
patronic_label.grid(column=0,row=2)

#  create patronic entry

patronic_text=StringVar()
patronic_entry=Entry(textvariable=patronic_text)
patronic_entry.grid(column=1,row=2)

#  credite size label and entry

# create credit size label

credit_size_label=Label(window,text="Размер кредита",font=("Arial",25))
credit_size_label.grid(column=0,row=3)

# credit size entry

creadt_size_text=StringVar()
credit_size_entry=Entry(textvariable=creadt_size_text)
credit_size_entry.grid(column=1,row=3)

credit_tern_label=Label(window,text="Размер кредита",font=("Arial",25))
credit_tern_label.grid(column=0,row=4)

creadt_size_text=StringVar()
credit_size_entry=Entry(textvariable=creadt_size_text)
credit_size_entry.grid(column=1,row=4)

#  create salary size  label and combobox

# create salary size combox
salary_size=Combobox()
salary_size['value']=(15000,20000,30000,35000,40000,45000,50000,55000,60000,65000,70000,750000,80000)
salary_size.grid(column=1,row=5)



window.mainloop()


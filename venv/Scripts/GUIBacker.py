from tkinter import*
from tkinter import messagebox



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


window.mainloop()


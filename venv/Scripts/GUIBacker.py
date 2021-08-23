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
name_entry=Entry(window, textvariable=name_text)
name_entry.grid(column=1,row=0)
window.mainloop()


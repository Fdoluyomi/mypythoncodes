import tkinter as tk
from tkinter import filedialog


def donothing():

 pass

def close():
 pass


def open():

    fd=tk.filedialog.askopenfile(mode='r')
    t=fd.read()
    entry.delete(0.0,tk.END)
    entry.insert('1.0', t)



def new():
  entry.delete(0.0,tk.END)

def save():
  fd=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
  content=entry.get('1.0', tk.END)
  fd.write(content)
 
 

def copy():
 pass

def edit():
 pass

root=tk.Tk()
root.title('Femis notepad')

icon=tk.PhotoImage(file='notepadlogo.png')
root.iconphoto(True,icon)

menubar=tk.Menu(root)
filemenu=tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='New',command=new)
filemenu.add_command(label='Open',command=open)
filemenu.add_command(label='Save As', command=save)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

menubar.add_cascade(label='File',menu=filemenu)

helpmenu=tk.Menu(menubar,tearoff=0)
helpmenu.add_command(label="Copy", command=copy)
menubar.add_cascade(label="Edit",menu=edit)





root.config(menu=menubar)

entry=tk.Text(root)
entry.pack()

root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      



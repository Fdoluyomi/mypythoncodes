import tkinter as tk
from tkinter import filedialog


def donothing():
# filewin=tk.Toplevel(root)
# button= tk.Button(filewin,text='Dont do anythin')
# button.pack()
 pass

def close():
 pass


def open():
 # tk.fi
  fd = filedialog.askopenfile(parent = root, mode = 'r')
  content= fd.read()
  
  entry.insert(0,content)

def new():
  entry.delete(0,8)

def save():
 fd=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
 content=entry.get()
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
filemenu.add_command(label='Save', command=save)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

menubar.add_cascade(label='File',menu=filemenu)

helpmenu=tk.Menu(menubar,tearoff=0)
helpmenu.add_command(label="Copy", command=copy)
menubar.add_cascade(label="Edit",menu=edit)





root.config(menu=menubar)

entry=tk.Entry( width=200,highlightbackground="black",highlightcolor="black")
entry.grid(row=0,column=0,columnspan=4,rowspan=20)
root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      



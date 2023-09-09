import tkinter as tk


def myfirst():
    print("You clicked a button")

root=tk.Tk()
#window.geometry("500X500")
root.title("Welcome to my program")

#widget button,label,imputetext,image

label=tk.Label(root,text="Femi",font=("Arial",40))
label.pack()

button=tk.Button(root,text="Submit button",command=myfirst,bg="black", fg="white")
button.pack()

root.mainloop()

#create a window with a title called I live in London and it must have a button and a Label
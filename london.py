import tkinter as tk


def myfirst():
    print("you clicked a button")

root=tk.Tk()
#window.geometry("500x500")
root.title("I live in London")

#widget button,label,imputext,image

label=tk.Label(root,text="This is London")
label.pack()

button=tk.Button(root,text="submit button",command=myfirst,bg="black",fg="white")
button.pack()

root.mainloop()
                    
                     




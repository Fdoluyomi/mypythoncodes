import tkinter as tk


firstnuber=None
secondnumber=None
operator=None

def get_text(number):
    entry.insert(10,number)
   # print(number)

def clear():
    entry.delete(0,8)
    print("Got heree")

def get_operator(op):
    global firstnuber,operator
    firstnuber= entry.get()
    operator=op
    entry.delete(0,8)

  
    

def docalculation():

    global firstnuber,secondnumber,operator
    secondnumber=entry.get()
   
    if(operator=='+'):
       answer= int(firstnuber)+int(secondnumber)
       entry.delete(0,8)
       entry.insert(0,answer)
    
    if(operator=='-'):
       answer= int(firstnuber)-int(secondnumber)
       entry.delete(0,8)
       entry.insert(0,answer)
    if(operator=='*'):
       answer=int(firstnuber) * int(secondnumber)
       entry.delete(0,8)
       entry.insert(0,answer)  

    if(operator=='/'):
        if(secondnumber=='0'):
            print('Cannot divide by Zezo')
            answer="Cannot divide by zero"
            entry.delete(0,8)
            entry.insert(0,answer)
        else:
         answer= int(firstnuber)/int(secondnumber)
         entry.delete(0,8)
         entry.insert(0,answer)
       

# print("Calculation to be done")

root=tk.Tk()
root.title("Femis Calculator")


icon=tk.PhotoImage(file="logo.png")
root.iconphoto(True,icon)

entry=tk.Entry()
entry.grid(row=0,column=0,columnspan=4)

btn7=tk.Button(text="7",font=("Arial",20),command=lambda:get_text("7"))
btn7.grid(row=1,column=0)

btn8=tk.Button(text="8",font=("Arial",20),command=lambda:get_text("8"))
btn8.grid(row=1,column=1)

btn9=tk.Button(text="9",font=("Arial",20), command=lambda:get_text("9"))
btn9.grid(row=1,column=2)

btnmult=tk.Button(text="*",font=("Arial",20),command=lambda:get_operator("*"))
btnmult.grid(row=1,column=3)



btn4=tk.Button(text="4",font=("Arial",20),command=lambda:get_text("4"))
btn4.grid(row=2,column=0)

btn5=tk.Button(text="5",font=("Arial",20),command=lambda:get_text("5"))
btn5.grid(row=2,column=1)

btn6=tk.Button(text="6",font=("Arial",20),command=lambda:get_text("6"))
btn6.grid(row=2,column=2)

btnminus=tk.Button(text="-",font=("Arial",20),command=lambda:get_operator("-"))
btnminus.grid(row=2,column=3)


btn1=tk.Button(text="1",font=("Arial",20),command=lambda:get_text("1"))
btn1.grid(row=3,column=0)

btn2=tk.Button(text="2",font=("Arial",20),command=lambda:get_text("2"))
btn2.grid(row=3,column=1)

btn3=tk.Button(text="3",font=("Arial",20),command=lambda:get_text("3"))
btn3.grid(row=3,column=2)

btnplus=tk.Button(text="+",font=("Arial",20),command=lambda:get_operator("+"))
btnplus.grid(row=3,column=3)

btn0=tk.Button(text="0",font=("Arial",20),command=lambda:get_text("0"))
btn0.grid(row=4,column=0)

btndot=tk.Button(text=".",font=("Arial",20))
btndot.grid(row=4,column=1)

btndiv=tk.Button(text="/",font=("Arial",20),command=lambda:get_operator("/"))
btndiv.grid(row=4,column=2)

btnequal=tk.Button(text="=",font=("Arial",20),command=docalculation)
btnequal.grid(row=4,column=3)

btnclear=tk.Button(text="C",font=("Arial",20),command=clear)
btnclear.grid(row=5,columnspan=4)


tk.mainloop()

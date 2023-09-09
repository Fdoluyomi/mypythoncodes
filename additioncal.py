question=input("What addition do you want to do \n")
#2+2
#print(question[1])
number1=int(question[0])
sign=question[1]
number2=int(question[2])

def calc(number1,number2):
    if(sign=="+"):
     return number1 + number2
    if(sign=="*"):
     return number1 * number2


print(calc(number1,number2))

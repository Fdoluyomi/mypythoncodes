def adddTwo(number):
    return number + 2

def doubleNumber(number):
    return number * 2


#print(adddTwo(4))

#print(doubleNumber(40))


add2=lambda number:number + 2

print(add2(13))

def add(number1,number2):
    
    return number1+number2




add_two=lambda number1,number2:number1 + number2

print(add_two(13,6))


add_three=lambda  number1,number2,number3:number1+number2 +number3

print(add_three(10,20,30))


def myfunc(n):
    return lambda a:a*n
    

mydoubler=myfunc(2)
mythripler = myfunc(3)


print(mythripler(30))



numbers=[2,6,10,20]

for number in numbers:
   
    print(number*2)

ages=[18,14,6,9,28,60,100]

def isAdult(age):
    if age >18:
        return True
    else: return False

#if number<100:


lambda age:age<18

print(isAdult(2))

adults=list(filter(lambda age:age<18,ages))


print(adults)




#print(doublenumbers)

def double(number):
    return number *2

b=lambda number:number*2

print(b(40))

for number in numbers:
    b=lambda number:number*2
    print(b(number))

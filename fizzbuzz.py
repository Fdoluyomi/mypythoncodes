#Write a Python program that iterates the integers from 1 to 50. 
#For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
#For numbers that are of three and five, print "FizzBuzz"

i=1
while i<50:
    if(i % 3==0 and i % 5==0):
      print("FizzBuzz", i)
    elif(i % 3==0):
      print("Fizz" ,i)
    elif(i % 5==0):
      print("Buzz" ,i)
    i=i+1
#user range to print. even numbers from 1 and 50
#Assignment use range to do the same thing
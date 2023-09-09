#meter to centimeter
def meter_to_centimeter(number_in_meter):
    return number_in_meter * 100

#answer=meter_to_centimeter(20)

#print("The answer is ", meter_to_centimeter(20))

meter=input("Enter your number in meters and I will convert it into centmeters \n")
answer_in_centimeters=meter_to_centimeter(int(meter))
print("The answer is ", answer_in_centimeters)
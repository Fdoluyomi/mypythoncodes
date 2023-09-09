#change from celcius to farenheight
# formula (0°C × 9/5) + 32
def celcius_to_farenheight(number_in_celcius):
    return (number_in_celcius * 9/5) + 32

answer = celcius_to_farenheight(100)
print("The answer is ",answer)

#write a function to change from farenheight to celcius
#change from farenheight to celcius
# formula (0°C × 9/5) + 32
def farenheight_to_celcius(number_in_farenheight):
    return (number_in_farenheight - 32) * 0.5556

answer = farenheight_to_celcius(87)
print("My answer is",answer) 
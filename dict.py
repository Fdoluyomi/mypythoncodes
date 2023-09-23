car={
    "brand":"ford",
    "model":"focus",
    "iselectric":False,
    "year":2020,
    "year":2023

}


person=dict(name="John",age=11,country="France")
#print(car["year"])

#print(len(car))

#print(car["iselectric"])
person["country"]="Italy"

print(person["country"])

car["colour"]="red"

#print(car.keys())
#print(car.values())
#car.pop("year")
#car.clear()
print(car.values())

if "model" in car:
    print("Yes model exiats")

for x in car.values():
    print(x)

print("Both keys and values")
for x,y in car.items():
    print(x,y)

# create a dictionarry of  dog
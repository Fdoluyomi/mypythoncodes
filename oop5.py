class Employee:


    def __init__(self,id:str,name:str,lastname:str,salary:int,age:int):
        self.id=id
        self.name=name
        self.lastname=lastname
        self.salary=salary
        self.age=age



employee1=Employee("American,Michael,Thomas,£20000,24")
employee2=Employee("English,Kyle,Walker21,£1000,21")
employee3=Employee("Christian,George,Jackson,24,£50000,29")

print(employee1.name)
print(employee2.name)
print(employee3.name)

                  








#create a class of employee ,id,firstname,lastname,salary,age
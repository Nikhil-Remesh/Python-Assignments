class Person:
    def __init__(self):
        self.name="nikhil"
        self.age=10
        self.address="Kannur,Kerala"
    def update(self):
        name=input("Enter new name: ")
        age=input("Enter new age: ")
        address=input("Enter new Address: ")
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print("the name is ",self.name)
        print("the age is ",self.age)
        print("the address is ",self.address)
        
p=Person()
p.display()
p.update()
p.display()

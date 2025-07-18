

# create a class for human 
# initialize name and weight 
# create a method display info 
# two objects

class Human:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def display(self):
        print(f"name is {self.name}")
        print(f"weight is {self.weight}")

class Animal(Human):
    def __init__(self,name,weight, color):
        super().__init__(name, weight)
        self.color = color   
    def display(self):
        return super().display()

if __name__ == "__main__":
    obj1 = Human("Abani", 23)
    obj1.display()
    obj = Animal("Dog",23, "black")
    obj.display()
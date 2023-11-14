# class add:
#     a = 10
#     b = 20
#     def ad(self):
#         print(self.a+ self.b)

# sum = add()
# sum.ad()
# print(sum.a + sum.b)


# class Add:
#     def __init__(self, a=10, b=20):
#         self.a = a
#         self.b = b
    
#     def ad(self):
#         print(self.a + self.b)

# sum = Add()
# sum.ad()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self,name,speak,colr):
        Animal.__init__(self,name)
        self.colr = colr
        self.speak = speak

    def speak(self):
        return f"{self.name} "

dog = Dog("Momin","Spike","Red")

print(dog.speak,dog.name,dog.colr) 
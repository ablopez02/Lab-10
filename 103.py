#Abbie Lopez and Emma
# I think that because this code is using th __str_ function, the output will take a string somewhere
#maybe print it like it is taking a string because the parantheses are a part of the string
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "("+str(self.age)+")"

p1 = Person("John", 36)
print(p1)

# global variable
name= "Global Name"
def myName():
    name="Rahul"
    def printName():
        nonlocal name
        name="Akash"
        print(name)
    printName()
    print(name)
    
myName()
print(name)
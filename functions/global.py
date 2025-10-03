name = "Gloabal Name"
def myName():
    name = "Rahul"
    def printName():
        global name
        name = "Akash"
        print(name)
    printName()
    print(name)
    
myName()
print(name)
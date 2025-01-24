class Computer:

    # This is a constructor. Will be called when the object is created
    def __init__(self, cpu, ram):
        print("Hello constructor")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Hello config ", self.cpu, self.ram)

# Created in heap memory
com1 = Computer("i5", 16)
print(type(com1))  # <class '__main__.Computer'>


# Here we are using the class name to call the method for the com1 object
Computer.config(com1)

# Behind the scene, it will pass the object as the first argument
com1.config()


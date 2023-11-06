class Person:
    def _int_(self, name, age, gender):
    #three attributes given to person class
        self.name = name
        self.age = age
        self.gender = gender
    #the _init_ method gets called when you create
    #a new object in a class. It takes 4 paramteres:
    #self, name, age, and gender... self refers to
    #the object itself and the other parameters are used
    #to initialize the attributes of the object
        def greet(self):
            print(f"Hello, my name is {self.name} and I am a {self.gender} person."
                )
                
person = Person("Alice", 30, "female")
person.greet() 
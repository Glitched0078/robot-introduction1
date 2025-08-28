class robot:
    height = 8
    color = "blue"
    name = "Kevin"
    
    def introduction(self):
        print("Hi im a robot")

    def details(self):
        print("My name is", self.name)
        print("I am", self.height, "meters tall")    
        print("I am", self.color)

ob = robot()
ob.introduction()
ob.details()        
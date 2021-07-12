class Calculator:
    num = 100  # class variable
    #default constructor
    def __init__(self, a, b):  # init should always be constructor name
        self.a = a  # a and b are Instance variable
        self.b = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.a + self.b + Calculator.num  # you can use Calculator.num



obj = Calculator(2, 3)   #syntax to create objects in Python
obj.getData()
print(obj.Summation())


obj1 = Calculator(4, 5)   #syntax to create objects in Python
obj1.getData()
print(obj1.Summation())


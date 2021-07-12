from OopsDemo import Calculator  # OopsDemo is filename


class ChildImpl(Calculator):  #place parent class name then import
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompletedata(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompletedata())


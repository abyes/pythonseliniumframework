#classes are basically prototype for example if you want to make a calculator so in classes you define
#what function it do like sum multiplaction etc
#no difference between functions and method if u use function inside a class its called method

#class variable are fixed and define in class where as instance variable are define in object and can be changed

class Method:
    y = 10


    def __init__(self,c,d):
        self.c = c
        self.d = d

    def sum(self):
        print(self.c + self.d)


# Creating an instance of the class with parameters
obj = Method(c=4,d=6)
obj.sum()

# Calling the sum method and printing the result

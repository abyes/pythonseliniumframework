#constructor jab hum define khd se krte hain init ke sath it means uski value hum run time pe provide krte hain
from oopconcept import Method

class Inher(Method):
        o = 4

        def __init__(self, c, d):
            super().__init__(c, d)
        def addition(self):
            print(self.o + Method.y)


       # Creating an instance of the child class with parameters
obj = Inher(c=3,d=4)
# Call the addition method
obj.addition()

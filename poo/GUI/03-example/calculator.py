# Logica de aplicación

class Calculator:
    def __init__(self):
        self.__number1 = 0
        self.__number2 = 0
        self.__operator = ""
        self.__active_number = 1

    @property
    def number1(self):
        return str(self.__number1)
    
    @number1.setter
    def number1(self,new_number):
        self.__number1 = float(new_number)

    @property
    def number2(self):
        return str(self.__number2)
    
    @number2.setter
    def number2(self,new_number):
        self.__number2 = float(new_number)

    def clean_number(self):
        self.__number1 = 0
        self.__number2 = 0
        # number = str(self.__number1)
        # new_number = number.rstrip(number[-1])

        # self.__number1 = float(new_number)

    def invert_number(self):
        #self.__number1 = self.__number1*(-1)
        self.__number1 *=-1

    def percent_number(self):
        #self.__number1 = self.__number1 / 100
        self.__number1 /= 100
    

    def add(self):
        added = self.__number1 + self.__number2
        self.__number1 = added
        self.__number2 = 0
        return added

    def sub(self):
        subs = self.__number1 - self.__number2
        self.__number1 = subs
        self.__number2 = 0
        return subs

    def mul(self):
        multiply = self.__number1 * self.__number2
        self.__number1 = multiply
        self.__number2 = 0
        return multiply

    def div(self):
        division = self.__number1 / self.__number2
        self.__number1 = division
        self.__number2 = 0
        return division

    def change_operator(self, operator):
        print("operator")
        self.change_operator = operator


    def calculate(self):
        if self.__operator == "+":
            self.add()
        elif self.__operator == "-":
            self.sub()
        elif self.__operator == "*":
            self.mul()
        elif self.__operator == "/":
            self.div()
        else:
            self.clean_number()
        
        self.__active_number = 1
        self.__operator = ""

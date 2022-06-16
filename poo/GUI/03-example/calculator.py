# Logica de aplicación

class Calculator:
    def __init__(self):
        self.__number1 = "0"
        self.__number2 = "0"
        self.__operator = ""
        self.__active_number = 1

    @property
    def number1(self):
        # if(isinstance(self.__number1,int)):
        #     return str(self.__number1)
        # elif(isinstance(self.__number1,float)):
        #     if(self.__number1.is_integer()):
        #         return str(int(self.__number1))
        #     else:
        #         return str(self.__number1)
        return self.__number1
    
    @number1.setter
    def number1(self,new_number):
        self.__number1 = new_number

    @property
    def number2(self):
        # if isinstance(self.__number2,int) or isinstance(self.__number2,float) and not self.__number2.is_integer():
        #     return str(self.__number2)
        # else:
        #     return str(int(self.__number2))
        return self.__number2
    
    @number2.setter
    def number2(self,new_number):
        # self.__number2 = float(new_number)
        self.__number2 = new_number

    @property
    def active_number(self):
        return self.__active_number

    def clean_number(self):
        self.__number1 = "0"
        self.__number2 = "0"
        self.__active_number = 1
        # number = str(self.__number1)
        # new_number = number.rstrip(number[-1])

        # self.__number1 = float(new_number)

    def invert_number(self):
        #self.__number1 = self.__number1*(-1)
        if self.active_number==1:
            number = float(self.number1)*-1
            if number.is_integer():
                self.__number1 = str(int(number))
            else:
                self.__number1 = number
        else:
            number = float(self.number2)*-1
            if number.is_integer():
                self.__number2 = str(int(number))
            else:
                self.__number2 = number

    def percent_number(self):
        #self.__number1 = self.__number1 / 100
        # self.__number1 /= 100
        if self.active_number==1:
            self.__number1 = float(self.number1)/100
        else:
            self.number2 = float(self.number2)/100
    

    def add(self):
        added = float(self.__number1) + float(self.__number2)
        self.__number1 = str(added)
        self.__number2 = "0"
        return added

    def sub(self):
        subs = float(self.__number1) - float(self.__number2)
        self.__number1 = str(subs)
        self.__number2 = "0"
        return subs

    def mul(self):
        multiply = float(self.__number1) * float(self.__number2)
        self.__number1 = f"{multiply:.2f}"
        # self.__number1 = "{:.2f}".format(multiply)

        self.__number2 = "0"
        return multiply

    def div(self):
        division = float(self.__number1) / float(self.__number2)
        self.__number1 = f"{division:.2f}"
        self.__number2 = "0"
        return division

    def change_operator(self, operator):
        print("operator")
        self.__operator = operator
        self.__active_number = 2

    def decimal_dot(self):
        if self.__active_number==1:
            self.__number1 = str(self.__number1)+"."
            print(self.__number1)
        else:
            self.__number2 = str(self.__number2)+"."
            print(self.__number2)


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

        # show_result(self)
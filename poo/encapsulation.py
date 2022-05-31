class User:
    def __init__(self, name, password, secret, money):
        self.name = name # Por defecto los atributos son publicos
        self.__password = password
        self.secret = secret
        self.__money = money # Atributo privado
    
    # @property
    # def password(self):
    #     pass

    # @password.setter
    # def password(self,new_password):
    #     self.__password = new_password

    def set_password(self,new_password):
        self.__password = new_password

    password = property(None,set_password)

    @property #getter
    def money(self):
        return "$"+str(self.__money)+" USD"

    @money.setter # Setter
    def money(self,new_value):
        if new_value<4000:
            self.__money = new_value
        else:
            print("Eso es mucho dinero!")
    
    #money = property(get_money,set_money)


tzuzul = User('Tzuzul', '12345', 'Me gustan las galletas', 100)

# tzuzul.__money = 1000000

tzuzul.money = 1000000

print(tzuzul.money)
tzuzul.money = 300
print(tzuzul.money)
tzuzul.money = 100000000000
print(tzuzul.money)

tzuzul.password = "54321"

print(tzuzul.__money)
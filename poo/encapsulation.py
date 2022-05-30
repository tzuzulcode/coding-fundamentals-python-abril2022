class User:
    def __init__(self, name, password, secret, money):
        self.name = name # Por defecto los atributos son publicos
        self.password = password
        self.secret = secret
        self.__money = money # Atributo privado

    def get_money(self):
        return "$"+str(self.__money)+" USD"

    def set_money(self,new_value):
        if new_value<4000:
            self.__money = new_value
        else:
            print("Eso es mucho dinero!")


tzuzul = User('Tzuzul', '12345', 'Me gustan las galletas', 100)

tzuzul.__money = 1000000

print(tzuzul.get_money())
tzuzul.set_money(3000)
print(tzuzul.get_money())
tzuzul.set_money(100000000000)
print(tzuzul.get_money())


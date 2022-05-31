class Cart:
    products_list = []
    products_amounts = []
    total = 0
    def __init__(self, name):
        self.name = name

    def add_to_cart(self,product,amount):
        if(product.amount>=amount):
            self.products_list.append(product)
            self.products_amounts.append(amount)
            #product.amount = product.amount - amount
            product.amount -= amount
        else:
            print("No hay suficiente cantidad disponible")

    def get_iva(self):
        pass

    def get_total(self):
        suma = 0
        for i in range(len(self.products_list)):
            product = self.products_list[i]
            amount = self.products_amounts[i]
            suma += product.get_total(amount)

        print(self.name)
        print(suma)


class Product:
    def __init__(self,amount,name,description,price):
        self.amount = amount
        self.name = name
        self.description = description
        self.price = price

    def get_total(self,amount):
        return amount*self.price


class Stock:
    list_products = []

    def add_to_stock(self,product):
        self.list_products.append(product)


product1 = Product(5,"Galletas","",10)
product2 = Product(10,"Agua","",8)

cart = Cart("Tzuzul")
cart.add_to_cart(product1,3)
cart.add_to_cart(product2,3)

print(cart.products_list)

cart.get_total()

print(product1.amount)
print(product2.amount)
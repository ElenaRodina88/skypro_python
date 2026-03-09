class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        print('Наименование:', self.name)

    def get_price(self):
        print('Цена:', self.price)

    def get_all(self):
        print('Product is:', self.name, 'Price is:', self.price)

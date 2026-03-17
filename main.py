class OnlineShop:
    shop_name = 'Tech Market'

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return f'Jami summa: {self.price * self.quantity}'

    @classmethod
    def change_shop_name(cls, new_name):
        if new_name != '':
            cls.change_shop_name = new_name

    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        else:
            return False


# obj1 = OnlineShop("Laptop", 1000, 2)
# print(obj1.total_price())
# OnlineShop.change_shop_name("Mega Tech")
# print(OnlineShop.shop_name)
# print(OnlineShop.is_valid_price(100))

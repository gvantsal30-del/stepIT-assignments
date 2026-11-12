class Product:
    """Represents every product in the store"""

    store_name = "TechShop Georgia" 
    currency = "GEL" 
    total_products = 0 

    def __init__(self, name, price, stock, category, discount=0):
        """
        Args:
            name (str): the product's name
            price (int): the product's price
            stock (int): the amount of each product
            category (str): the product's category
            discount (0): discount on the product
            """

        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.discount = discount
        Product.total_products += 1
    
    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Category: {self.category}, Discount: {self.discount}%"
    def apply_discount(self, percent):
        self.discount = percent
        print(f"Discount updated to {self.discount}%")
    def update_stock(self, amount):
        self.stock += amount
        if self.stock <0:
            print("Stock can not be below zero")
        else:
            print(f"Stock updated: {self.stock}")
    def calculate_final_price(self):
        final_price = self.price - (self.price * self.discount / 100)
        return final_price
    @classmethod
    def get_total_products_count(cls):
        return cls.total_products

p1 = Product("Smartphone X", 1200, 15, "Electronics")
p2 = Product("Wireless Headphones", 250, 30, "Electronics", discount=10)
p3 = Product("Running Shoes", 180, 8, "Sportswear")

print(p1.get_info())
p1.apply_discount(15)
print(f"საბოლოო ფასი ფასდაკლებით: {p1.calculate_final_price()} {Product.currency}")

p3.update_stock(5) 
p3.update_stock(-2) 

print(f"სულ შექმნილი პროდუქტები: {Product.get_total_products_count()}")
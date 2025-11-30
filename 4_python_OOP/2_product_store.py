''' 
    Design and Create and online store for products(name, price) 
    Track total product being created.
    Create a static method to calculate discount on each product based on a % parameter
'''

class Product:

    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self): #instance method
        print(f"{self.name} is Rs.{self.price}.")

    @classmethod  # class method
    def get_count(cls):
        print(f"total product in store: {cls.count}")

    @staticmethod # static method
    def get_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(final_price)
    
p1 = Product("phone", 10_000)
p2 = Product("laptop", 50_000)
p3 = Product("watch", 5_000)

p1.get_info()
Product.get_count()  # p1.get_count() we can also access the class attribute from object.
p1.get_discount(p1.price,10)
class Items():
    pay_rate = 0.8
    def __init__(self, name:str, price:float,quantity=0):
        assert price >= 0, f"The price {price} is less than or equals to 0."
        assert quantity >= 0, f"The quantity {quantity} is less than or equals to 0."
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_cost =self.price * self.quantity
        print(f"The total Quantity of {self.name} is {self.total_cost}")
        print(f"AN INSTANCE {name} IS CREATED")
    def apply_Discount(self):
        self.price = self.price * self.pay_rate


print("\t")
Items1=Items("Samsung",1500,10)
Items1.apply_Discount()
print(f"20% discount applied . Amount payable: {Items1.price}")
# Items1.quantity = 10
# print(Items1.calculate_total_cost(Items1.price,Items1.quantity))

print("\t")

Items2=Items("Iphone",3500,20)
Items2.apply_Discount()
pay_rate = 0.8
print(f"20% discount applied . Amount payable: {Items2.price}")
# Items1.quantity = 25
# print(Items1.calculate_total_cost(Items1.price,Items1.quantity))
#

# print(Items1.total_cost)
# print(Items2.total_cost)

item1 = Items("Phone", 100, 1)
print("\t")
item2 = Items("Laptop", 1000, 3)
print("\t")
item3 = Items("Cable", 10, 5)
print("\t")

item4 = Items("Mouse", 50, 5)
print("\t")

item5 = Items("Keyboard", 75, 5)
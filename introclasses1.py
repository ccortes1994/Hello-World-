'''
create a simple class
attributes - variables
methods - functions working usually with attributes
'''

class CashRegister :
    global rate #global variables
    rate = 0.078
    def __init__(self):
        #attributes
        self.items = 0
        self.price = 0

    #methods
    def update_register(self, price):
        self.items = self.items + 1
        self.price = self.price + price

    def display_register(self):
        return print('The number of items ',self.items,'\n Total price without taxes ', self.price,'Rate for taxes ', rate)

    def clear_register(self):
        CashRegister.final_price_tax(self)

        self.items = 0
        self.price = 0

    def final_price_tax(self):
        self.price = (1 + rate)*self.price
        return print('The price including taxes ', round(self.price,2))
    def discount(self):














#start
regeister1 = CashRegister()
register1.update_register(100.00)
register1.update_register(2.95)
register1.update_register(125.75)
register1.update_register(9.99)
#register1.final_price_tax()

register1.display_register()
register1.clear_register()


# register1 = CashRegister()
# register1.update_register(1.95)
# register1.update_register(.65)
# register1.update_register(99.99)
# register1.update_register(25000.00)
# #print('Clear register 1')
# #miss
# register1.update_register(2.09)
# register1.display_register()
#
# #print('register2')
# register2 = CashRegister()
# register2.display_register()
# register2.update_register(499.99)
# print(register2.price)


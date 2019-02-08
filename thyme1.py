name = "Dean"
sex = "Male"
max_hit_points = 50
current_hit_points = 50
max_speed = 10

def display_character(name, sex, max_hit_points, current_hit_points, max_speed):
    print(name, sex, max_hit_points, current_hit_points, max_speed)

class Character(): #class names are capitalized
    """ This is a class that represents the main character in the game."""
    def __init__(self):
        """ This is a method that sets up the variable in the object."""
        self.name = "Dean"   #attriutes or fields
        self.sex = "Male"
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10
        self.armor_amount = 8
class Address():
    """Hold all the fields for a mailing address."""
    def __init__(self):   # a constructor
        """ Set up the address fields."""
        self.name = " "
        self.line1 =" "
        self.line2 = " "
        self.city = " "
        self.state = " "
        self.zip = " "

# example 1

home_address = Address()

home_address.name = "Dean Winchester"
home_address.line1 = "240 S. Castiel Street"
home_address.line2 = "The Family Business Building"
home_address.city = "Lebanon"
home_address.state = "KS"
home_address.zip = "19067"

print("The dog's owner lives in " + home_address.city + ".")
print("The onwer's name is " + home_address.name)
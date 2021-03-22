class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe__restaurant(self):
        print("Você pode comer " + self.cuisine_type + " no " + self.restaurant_name.title())
        


    def open_restaurant(self):
        print("O " + self.restaurant_name.title() + " está aberto!")



    
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    
    def print_flavors(self):
        print("os sabores são: ")
        for flavor in self.flavors:
            print(flavor)
        

restaurant = Restaurant('Julinho cachorrão','podrão')
restaurant.describe__restaurant()
restaurant.open_restaurant()

beijobeijo = IceCreamStand('Beijo Beijo', 'sorveteria' , ['chocolate','morango','creme'])
beijobeijo.print_flavors()

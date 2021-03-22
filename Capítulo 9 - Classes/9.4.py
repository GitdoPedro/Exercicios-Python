class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe__restaurant(self):
        print("Você pode comer " + self.cuisine_type + " no " + self.restaurant_name.title())
        


    def open_restaurant(self):
        print("O " + self.restaurant_name.title() + " está aberto!")


    def read_order_served(self):
        print("O restaurante serviu " + str(self.number_served )+ " pessoas")
        
    def set_number_served(self,clients):
        self.number_served = clients
    
    def increment_number_served(self,clients):
        self.number_served +=clients    
    

restaurant = Restaurant('Julinho cachorrão','podrão')
restaurant.describe__restaurant()
restaurant.open_restaurant()
restaurant.read_order_served()
restaurant.set_number_served(50)
restaurant.read_order_served()
restaurant.increment_number_served(100)
restaurant.read_order_served()

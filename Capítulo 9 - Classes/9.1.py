class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe__restaurant(self):
        print("Você pode comer " + self.cuisine_type + " no " + self.restaurant_name.title())
        


    def open_restaurant(self):
        print("O " + self.restaurant_name.title() + " está aberto!")



    


    

restaurant = Restaurant('Julinho cachorrão','podrão')
restaurant.describe__restaurant()
restaurant.open_restaurant()

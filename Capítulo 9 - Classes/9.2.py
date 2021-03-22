class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe__restaurant(self):
        print("Você pode comer " + self.cuisine_type + " no " + self.restaurant_name.title())
        


    def open_restaurant(self):
        print("O " + self.restaurant_name.title() + " está aberto!")



    


    

restaurant1 = Restaurant('Julinho cachorrão','podrão')
restaurant1.describe__restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('Mc donalds','podrão')
restaurant2.describe__restaurant()
restaurant2.open_restaurant()


restaurant3 = Restaurant('papa jack','pizza')
restaurant3.describe__restaurant()
restaurant3.open_restaurant()

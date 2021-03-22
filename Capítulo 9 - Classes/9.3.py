class User():
    def __init__(self,first_name,last_name,age,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        name = self.first_name + " " + self.last_name
        print(name.title()+ " tem " + self.age  + " anos e é do sexo " + self.sex)



    def greet_user(self):
        print("E aí , " + self.first_name + ", firmeza ?")


pedro = User('pedro','lima','30','masculino')
pedro.describe_user()
pedro.greet_user()

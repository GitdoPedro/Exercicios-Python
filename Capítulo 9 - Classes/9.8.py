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


class Admin(User):
    def __init__(self,first_name, last_name,age,sex,privileges):
        super().__init__(first_name, last_name,age,sex)
        self.privileges = privileges


class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Esse usuário pode: ")
        for privilege in self.privileges:
            print(privilege)

pedro = User('pedro','lima','30','masculino')
pedro.describe_user()
pedro.greet_user()
privilege = Privileges(['can delete post','can update post'])

admin = Admin('Plinio', 'neto', 33, 'm', privilege)

admin.privilege.show_privileges()

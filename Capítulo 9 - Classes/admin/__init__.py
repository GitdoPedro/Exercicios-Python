

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

from admin import *
pedro = User('pedro','lima','30','masculino')
pedro.describe_user()
pedro.greet_user()
privilege = Privileges(['can delete post','can update post'])

admin = Admin('Plinio', 'neto', 33, 'm', privilege)




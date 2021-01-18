new_users = ['zico','adilio','junior','andrade','lico']

current_users = ['zico','pet','junior','adriano','gabigol']


for current_user in current_users:
    if current_user.lower() in new_users:
        print(current_user+" já foi utilizado")


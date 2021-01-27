def show_magicians(names):
    for name in names:
        print(name.title() + " is a magician!\n")



def change_magicians(names,new_names):
    for name in names:
        new_name  =  'grande ' + name
        new_names.append(new_name)
        


magicians = ['mister m','fu manchu','dai vernon','david blaine']
big_magicians = []



show_magicians(magicians)
change_magicians(magicians,big_magicians)
show_magicians(big_magicians)

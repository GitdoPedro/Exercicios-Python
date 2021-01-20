rios = {
    'nilo'     : 'egito',
    'amazones' : 'brasil',
    'paraguai' : 'paraguai',
    'orinoco'  : 'venezuela',
    'missouri' : 'estados unicdos'

}



for rio,pais in rios.items():
    print('O rio '+ rio.title() + ' corre pelo(a) ' + pais.title())
    

for rio in rios.keys():
    print ('O rio ' + rio.title() + ' é conhecido mundialmente')

for pais in rios.values():
    print(pais.title() + ' possui um rio famoso')

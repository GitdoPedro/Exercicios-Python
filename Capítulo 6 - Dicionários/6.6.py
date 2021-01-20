rios = {
    'nilo'     : 'egito',
    'amazones' : 'brasil',
    'paraguai' : 'paraguai',
    'orinoco'  : 'venezuela',
    'missouri' : 'estados unicdos'

}

riosFamosos = {'nilo','negro','danúbio'}


for rio in riosFamosos:
    if rio not in rios.keys():
        print(rio.title() + ' não está na lista')
    else:
        print(rio.title() + ' já foi adicionado à lista')

    

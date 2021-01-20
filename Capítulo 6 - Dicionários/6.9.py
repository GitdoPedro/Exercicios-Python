favorite_places = {
    'pedro'    : ['parque tanguá','macaranã','reserva'],
    'veronica' : ['flores da tijuca','grajaú','casa do pedrinho'],
    'lucas'    : ['são januário','prado júnior','mario claudio']

}
for people,places in favorite_places.items():
    print(people.title() + ' visita: \n' )
    for place in places:
        print(place)

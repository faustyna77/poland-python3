rooms = {
    'start': {'rooms': ['1'], 'items':[]},
    '1': {'rooms': ['start', '2', '3'], 'items':[]},
    '2': {'rooms': ['1'], 'items':['key']},
    '3': {'rooms': ['1', '4'], 'items':[]},
    '4': {'rooms': ['3', '5'], 'items': []},
    '5': {'rooms': ['4', 'Exit'], 'items':[]}
}



room = 'start'
key = False
while True:

    print('jesteś w pokoju: ', room)
    for newroom in rooms[room]['rooms']:
        print('Możesz iść do pokoju:', newroom)
    newroom = input('Który pokój wybierzesz? ')
    if newroom not in rooms[room]['rooms']:
        print('Ten pokój nie istnieje!')
        time.sleep(2)
        continue
    if newroom == 'Exit' and not key:
        print('nie masz klucza!!!')
        continue
    if newroom == 'Exit': 
        print("wygrałes")
    room = newroom # tutaj był błąd gdyż przypisanie room do aktualnego pokoju newroom było w ifie a powinno byc poza tym ifem 
    
    if 'key' in rooms[room]['items']:
        key = True
        print('znalazłeś klucz')
        rooms[room]['items'].remove('key')
print('')
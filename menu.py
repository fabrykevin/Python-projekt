
def menu():
    option=-1
    while option< 0 or option>4:
        print('---------------------')
        print('0 - Regisztráció') 
        print('1 - Az összes cipő megmutatása')
        print('2 - A Kedvenc cipő megkeresése ')
        print('3 - A legdrágább és a legolcsóbb cipők megmutatása ')
        print('4 - Legújabb és a legrégebbi cipők megmutatása ')
        print('---------------------')
        option=int(input('Válasszon a lehetőségek közül :'))
    return option

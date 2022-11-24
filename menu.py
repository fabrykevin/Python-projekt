
def menu():
    option=-1
    while option< 0 or option>5:
        print('---------------------')
        print(' 1 - Regisztráció') 
        print(' 2 - A teljes kínálat megmutatása')
        print(' 3 - A Kedvenc cipő megkeresése ')
        print(' 4 - A legdrágább és a legolcsóbb cipők megmutatása ')
        print(' 5 - Legújabb és a legrégebbi cipők megmutatása ')
        print(' 6 - Kilépés')
        print('---------------------')
        option=int(input('Válasszon a lehetőségek közül :'))
    return option

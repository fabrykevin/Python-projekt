
def menu():
    option=-1
    while option< 0 or option>5:
        print('------------')
        print('0 - Regisztráció') 
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - Legújabb cipő és a legrégebbi cipő ')
        print('------------')
        option=int(input('Válasszon a lehetőségek közül :'))
    return option

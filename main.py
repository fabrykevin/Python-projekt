from menu import *
from fuggvenyek import showall, readFile, search

readFile()
choice=-1
while choice != 0:
    choice=menu()
    if choice == 1:
        showall()
    elif choice == 2:
        cipok=input('Kérem a cipőt')
        result=search(cipok)
        if len(result)==0:
            print('Nincs ilyen cipő.')
        else:
            for item in result:
                print(f'\t{item}')
    elif choice == 3:
        legolcsobb(), legdrágább() 
    elif choice == 4:
        Legújabb() , legrégebbi()
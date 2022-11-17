from regisztracio import signup, login
from menu import*
from fuggvenyek import *
Nevek=[]

def regisztracio():
    email=input('Adja me az e-mail címet: ')
    password=input('Adja meg a jelszót')
    megerosit=input('Jelszó megerősítés')
    if megerosit == password:
        signup(email, password)
        print('Sikeres regisztráció')
    
    else:
        print('A jelszó nem egyezik! \n')

def bejelentkezesek():
    email=input('Kérem az e-mail címet: ')
    password=input('Kérem a jelszót')
    
    login(email, password)
    for row in Nevek:
        splittedData=row.split(';')
    
    if email==splittedData[0] and password==splittedData[1]:
        print('Sikeres bejelentkezés!')       




readFile()
choice=-1
while choice != 0:
    choice=menu()
    if choice == 1:
        showall()
    elif choice == 2:
        cipok=input('Kérem a cipőt: ')
        result=search(cipok)
        if len(result)==0:
            print('Nincs ilyen cipő.')
        else:
            for item in result:
                print(f'\t{item}')
    #elif choice == 3:
    #    legolcsobb(), legdrágább() 
    #elif choice == 4:
     #   Legújabb() , legrégebbi()
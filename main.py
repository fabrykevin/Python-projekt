from regisztracio import signup, login
from menu import*
from fuggvenyek import *
neveklist=[]

def reg():
    email=input('Adja me az e-mail címet: ')
    pwd=input('Adja meg a jelszót')
    conf_pwd=input('Jelszó megerősítés')
    if conf_pwd == pwd:
        signup(email, pwd)
        print('Sikeres regisztráció')
    
    else:
        print('A jelszó nem egyezik! \n')

def bejelentkezesek():
    email=input('Kérem az e-mail címet: ')
    pwd=input('Kérem a jelszót')
    
    login(email, pwd)
    for row in neveklist:
        splitted=row.split(';')
    
    if email==splitted[0] and pwd==splitted[1]:
        print('Sikeres bejelentkezés!')       




readFile()
choice=-1
while choice != 0:
    choice=menu()
    #if choice == 1:
    #    showall()
    #elif choice == 2:
    #    cipok=input('Kérem a cipőt: ')
    #    result=search(cipok)
    #    if len(result)==0:
    #        print('Nincs ilyen cipő.')
    #    else:
    #        for item in result:
    #            print(f'\t{item}')
    #elif choice == 3:
    #    legolcsobb(), legdrágább() 
    #elif choice == 4:
     #   Legújabb() , legrégebbi()
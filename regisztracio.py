from main import *
Nevek=[]


def signup(email, password):
    file=open('nevek.csv', 'r', encoding='utf-8')

    for row in file:
        Nevek.append(row.strip())
    
    file.write(email + ';')
    file.write(password +  ';' )
    
    file.close()

def login(email, password):
    file=open('nevek.csv', 'r', encoding='utf-8')


    for row in file:
        Nevek.append(row.strip())

    file.close()

    
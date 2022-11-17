from main import *
neveklist=[]


def signup(email, password):
    file=open('nevek.csv', 'r+', encoding='utf-8')

    for row in file:
        neveklist.append(row.strip())
    
    file.write(email + ';')
    file.write(password +  ';' )
    
    file.close()

def login (email, pwd):
    file=open('nevek.csv', 'r', encoding='utf-8')


    for row in file:
        neveklist.append(row.strip())

    file.close()

    
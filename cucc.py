from menu import*
from main import*
from fuggvenyek import*

sneaker = []

def load():
    file = open('Sneaker.csv','r',encoding='utf-8')

    for row in file:
        sneaker.append(row.stip())
    file.close()

def showAll():
    print('Összes sneaker')
    for sneaker in sneaker:
        print(sneaker, end = ' ')
    print()



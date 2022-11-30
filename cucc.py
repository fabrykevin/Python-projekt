from menu import *
from main import *
from fuggvenyek import *
from nevek import *

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

def smallest():
    min = 9999999999
    first = sneaker[1].split(';')
    minSize = int(first[4])
    minName = first[1]
    for sneaker in sneaker:
        sneakerData = sneaker.split(';')
        if minSize > int(sneakerData[4]):
            minSize = int(sneakerData[4])
            minName = sneakerData[1]


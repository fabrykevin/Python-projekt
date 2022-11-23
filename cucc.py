from menu import *
from main import *
from fuggvenyek import *
from nevek import *
from fileHandling import *

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

def lowest():
    for x in shoes:
        lowest = 99999999999999999
        shoe = ""
        splittedData = x.split(";")
        if splittedData{6} < int(lowest):
            shoe = splittedData{0}
            lowest = splittedData{6}
    return lowest
        


def highest():
    for x in shoes:
        highest = 0
        shoe =""
        splittedData = x.split(";")
        if splittedData{6} > int(highest):
            shoe = splittedData{0}
            highest =splittedData{6}
    return highest
from nevek import *

def registration(startNumber):
    for nevek in nevek:
        nameList = nevek.split(';')
        if nameList[0] == startNumber:
            return nameList[6]
    return False

<<<<<<< HEAD
def searchBrand(márka):
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    splittedData = file
=======



>>>>>>> ede0fbabecaf85dce9fd4d69c02571281d1179e1

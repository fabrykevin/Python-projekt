from nevek import *
from Sneaker import *

def registration(startNumber):
    for nevek in nevek:
        nameList = nevek.split(';')
        if nameList[0] == startNumber:
            return nameList[6]
    return False

def searchBrand(results, márka):
    for item in results:
        if item.name == márka:
            return item
    return False

from Nevek import nevek

def registration(startNumber):
    for nevek in nevek:
        nameList = nevek.split(';')
        if nameList[0] == startNumber:
            return nameList[6]
    return False

def searchBrand(márka):
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    

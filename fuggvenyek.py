from Nevek import nevek

def registration(startNumber):
    for nevek in nevek:
        nameList = nevek.split(';')
        if nameList[0] == startNumber:
            return nameList[6]
    return False

def searchBrand(results, márka):
    for index,item 

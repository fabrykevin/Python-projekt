from Nevek import nevek

data = []

def registration(startNumber):
    for nevek in nevek:
        nameList = nevek.split(';')
        if nameList[0] == startNumber:
            return nameList[6]
    return False

def readfile():
    file = open('Sneaker.csv', 'r', encoding='utf-8')

    for row in file:
        data.append(row.strip())

    file.close()

def searchBrand():
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    splittedData = row.split(';')
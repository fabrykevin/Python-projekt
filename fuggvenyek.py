from Nevek import nevek

def registration(startNumber):
    for nevek in nevek:
        nameList = nevek.split(';')
        if nameList[0] == startNumber:
            return nameList[6]
    return False

<<<<<<< HEAD


def    bejelentkezes


=======
def searchBrand(márka):
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    splittedData = file
>>>>>>> 02686cf3c457afd19bc24d33a7f4d8ed57ecc408

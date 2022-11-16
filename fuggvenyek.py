from nevek import *
def readFile():
    file =  open('Sneaker.csv','r', encoding='utf-8')
    firstRow=file.readline()
    for row in file: 
      
        file.close()

def registration(startNumber):
    for nevek in nevek:
        nameList = nevek.split(';')
        if nameList[0] == startNumber:
            return nameList[6]
    return False



def    bejelentkezes



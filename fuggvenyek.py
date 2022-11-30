from fileHandling import *

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


data=[]
def readFile():
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    for row in file:
        data.append(row.strip().split(";"))
    print(* data, sep = "\n")
    file.close

def searchSizeByType():
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    file.readline()
    Brand = input("Adja meg a cipő márkáját: ").upper()
    Type = input("Add meg a cipő típusát: ").upper()
    for row in file:
        splitted = row.split(';')
        if splitted[1] == Brand and splitted[2] == Type:
            print(f'{splitted[4]}')

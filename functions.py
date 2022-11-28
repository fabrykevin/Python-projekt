data=[]
def readFile():
    file = open('sneaker.csv', 'r', encoding='utf-8')
    for row in file:
        data.append(row.strip())
    
    file.close


def login():
    user=input('Felhasználónév:')
    pwd=input('Jelszó:')
    f=open('nevek.csv', 'r'  )
    for line in f.readlines():
        us,pw =line.strip().split(';')
        if (user in us) and (pwd in pw):
            print('Sikeres')
            return True

def signup():
    file=open('nevek.csv', 'a', encoding='utf-8')
    username=input('új Felhasználónév:')
    password=input('új jelszó:')
    term=input('szerződés elfogadás/elutasítás: ')
    if term=='elfogadás':
        print('regisztráció sikeres')
        file.write(f'{username}; {password} \n')
    elif term=='elutasítás':
        print('sikertelen regisztráció')
    else:
        print('Nincs ilyen opció')

def legdrágábbcipo():
    file=open('Sneaker.csv', 'r', encoding='utf-8')
    file.readline()
    legnagyobb=0
    for row in file:
        splitted=row.split(';')
        if int(splitted[6])> legnagyobb:
            legnagyobb=int(splitted[6])
    file.close()
    return legnagyobb[ 2 , 6 ] 


def legolcsobbcipo():
    file=open('Sneaker.csv', 'r' , encoding='utf-8')
    file.readline()
    legkisebb=9999999
    for row in file:
        splitted=row.split(';')
        if int(splitted[6])> legkisebb:
            legkisebb=int(splitted[6])
    file.close
    return legkisebb[ 2 , 6 ]



def legujabbcipo():
    file=open('Sneaker.csv', 'r', encoding='utf-8')
    file.readline()
    legnagyobb=0
    for row in file:
        splitted=row.split(';')
        if int(splitted[7])> legnagyobb:
            legnagyobb=int(splitted[7])
    file.close()
    return legnagyobb[ 2 , 7 ] 



def legregebbi():
    file=open('Sneaker.csv', 'r' , encoding='utf-8')
    file.readline()
    legkisebb=9999999
    for row in file:
        splitted=row.split(';')
        if int(splitted[7])> legkisebb:
            legkisebb=int(splitted[7])
    file.close
    return legkisebb[ 2 , 7 ]



 

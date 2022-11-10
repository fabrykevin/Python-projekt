data=[]
def readFile():
    file =  open('nevek.csv','r', encoding='utf-8')
    firstRow=file.readline()
    for row in file: 
      
        data.append(row.strip())
    file.close()


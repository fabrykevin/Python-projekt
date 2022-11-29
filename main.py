from menu import *
from functions import *
from fuggvenyek import *
import os
from fileHandling import *
current_directory = os.getcwd()
print('}----------Üdvözöljük----------{')
print('}----A Sneaker Simulátorban----{')
readFile()
choice=-1
while choice != 0:
        choice=menu()
        if choice == 1:
            signup(), login()
        elif choice == 2:
            #showall()
            readFile()
            #print(current_directory)
        elif choice == 3:
            searchSizeByType()

        elif choice==4:
            
            legdrágábbcipo(),  legolcsobbcipo()
           

        elif choice==5:
            legujabbcipo() ,  legregebbi()
        

            
            



        
            


            





      
    

   
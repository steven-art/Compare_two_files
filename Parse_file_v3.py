# -*-coding:utf-8 -*

import difflib


#recupere le nom des deux fichier a comparer
fname1 = 'fichier1.txt'
fname2 = 'fichier2.txt'

#ouverture des deux fichiers
f1 = open(fname1,'r')
f2 = open(fname2,'r')
fichier  = open('conffinal.txt','w')
# Print confirmation
print("-----------------------------------")
print("Comapraison des fichiers ", " > " + fname1, " < " +fname2, sep='\n')
print("-----------------------------------")

# lecture de la premiére ligne du fichier
f1_line = f1.readline()


#initialisation des variables
li = 1
li2 = 1

#Boucle de parsage de fichier 2 par rapport au fichier 1
while f1_line != '' :
    if f1_line in f2 :
        fichier.write(f1_line.rstrip() + '\n')     
    elif f1_line is not f2:
        fichier.write(f1_line.rstrip() + '\n')
        print("1 : >+", "Line-%d" % li, f1_line.rstrip())
        
    li +=1 
    f1_line = f1.readline()    
        
       
    

#Boucle de parsage de fichier 1 par rapport au fichier 2
f2_line = f2.readline()
while f2_line != '':
    if f2_line is not f1:
        print("2 : <", "Line-%d" % li2, f2_line.rstrip())
    
    #lit la ligne suivante des fichiers
    f2_line = f2.readline()
    #increment le compteur de ligne
    li2 += 1




# fermeture des fichiers
fichier.close()
f1.close()
f2.close()

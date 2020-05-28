# -*-coding:utf-8 -*

import difflib


#recupere le nom des deux fichier a comparer
fname1 = input("Enter the first filename: ")
fname2 = input("Enter the second filename: ")

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
f2_line = f2.readline()

# Initialisation d'un compteur
li = 1
li2 =1

# Boucle permettant de comparer les deux fichiers ligne par ligne
while f1_line != '' or f2_line != '':

    # Strip the leading whitespaces
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
        
    #comparaison des lignes 
    if f1_line == f2_line :
        fichier.write(f1_line + '\n')

    elif f2_line == '' and f1_line != '':
        print("1 : >+", "Line-%d" % li, f1_line)
        fichier.write(f1_line + '\n')
    
    elif f1_line == '' and f2_line != '':
        print("2 : <+", "Line-%d" % li2, f2_line)
        fichier.write(f2_line + '\n')
    
    elif f1_line != '' and f2_line != '':
        
        
        while f1_line != f2_line :
            fichier.write(f1_line + '\n')
            print("1 : >+", "Line-%d" % li, f1_line)
            print("2 : <", "Line-%d" % li2, f2_line)
            f1_line = f1.readline()
            f2_line = f2.readline()
            li += 1
            li2 += 1 
            
            if f1_line == f2_line :
                fichier.write(f1_line + '\n')
                f1_line = f1.readline()
                f2_line = f2.readline()
                  
            else :
                fichier.write(f1_line + '\n')
                print("1 : >+", "Line-%d" % li, f1_line)
                f1_line = f1.readline()
                li +=1
                li2 += 1
    
    
    #lit la ligne suivante des fichiers
    f1_line = f1.readline()
    f2_line = f2.readline()


    #increment le compteur de ligne
    li += 1
    li2 += 1
# fermeture des fichiers
fichier.close()
f1.close()
f2.close()

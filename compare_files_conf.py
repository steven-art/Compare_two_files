import difflib


# Rentrer le non des deux fichiers
newFile = input("Enter the new filename: ")
oldFile = input("Enter the old filename: ")

# Print confirmation
print("-----------------------------------")
print("Comapraison des fichiers ", " > " + newFile, " < " +oldFile, sep = '\n')
print("-----------------------------------")

#ouverture des deux fichiers
fnewLine =  open(newFile).readlines()
foldLine =  open(oldFile).readlines()
fichier  = open('conffinal.txt','w')

#faire la différence entre les deux fichiers et mettre la différence dans un fichier html
diff = difflib.HtmlDiff().make_file(fnewLine, foldLine, newFile, oldFile)
difference_report = open('different_report.html','w')
difference_report.write(diff)

print("- Prenez le fichier different_report.html que vous avez vu apparaitre.")
print("- Ouvrez ce fichier sur un navigateur web.")

difference_report.close()

#ouverture des deux fichiers
f1 = open(newFile,'r')
f2 = open(oldFile,'r')

# lecture de la premiére ligne du fichier
f1_line = f1.readline()
f2_line = f2.readline()

# Initialisation d'un compteur
li = 1
li2 =1
difference = False
# Boucle permettant de comparer les deux fichiers ligne par ligne
while f1_line != '' or f2_line != '':

    # enlever les espaces au debut et à la fin de chaque ligne
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
    
    if f1_line == '' and f2_line != '':
        difference = True
        fichier.write(f2_line + '\n')
    elif f1_line != f2_line : 
        fichier.write(f1_line + '\n')
        difference = True
    else:
        fichier.write(f1_line + '\n')

    #lit la ligne suivante des fichiers
    f1_line = f1.readline()
    f2_line = f2.readline()


    #increment le compteur de ligne
    li += 1
    li2 += 1     
#premet d'indiquer qu'une différence est présent
if difference == True:
    print("-----------------------------------")
    print("- différences detectées, vous pouvez consulter le fichier :  different_report.html" )
else:
    print("-----------------------------------")
    print("Les fichiers sont identiques")
# fermeture des fichiers
fichier.close()
f1.close()
f2.close()
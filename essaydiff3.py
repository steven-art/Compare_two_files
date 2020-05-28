import difflib


# Rentrer le non des deux fichiers
newFile = input("Enter the first filename: ")
oldFile = input("Enter the second filename: ")

# Print confirmation
print("-----------------------------------")
print("Comapraison des fichiers ", " > " + newFile, " < " +oldFile, sep = '\n')
print("-----------------------------------")

#ouverture des deux fichiers
fnewLine =  open(newFile).readlines()
foldLine =  open(oldFile).readlines()


#faire la différence entre les deux fichiers et mettre la différence dans un fichier html
diff = difflib.HtmlDiff().make_file(fnewLine, foldLine, newFile, oldFile)
différence_report =open('diffrent_report.html','w')
différence_report.write(diff)

print("- Prenez le fichier diffrent_report.html que vous avez vu apparaitre.")
print("- Ouvrez ce fichier sur un navigateur web.")


différence_report.close()
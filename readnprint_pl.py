#Plik wyszukiwany musi być w tym samym folderze co ten program
#Pyta o nazwę pliku
fname = input("Enter file name: ")
#próbuje otworzyć plik
try:
    fh = open(fname)

    
#Jeśli nie znajdzie pliku drukuje należny komunikat
except:
    print("File not found")
    quit()
#Drukuje treść pliku dużymi literami i bez zbędnej spacji
for line in fh:
    line = line.upper()
    line = line.rstrip()
    print(line)
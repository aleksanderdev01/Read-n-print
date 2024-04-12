#The file hello.txt is in the same folder as the file of python code
fname = input("Enter file name: ")
try:
    fh = open(fname)
    
except:
    print("File not found")
    quit()

for line in fh:
    line = line.upper()
    line = line.rstrip()
    print(line)
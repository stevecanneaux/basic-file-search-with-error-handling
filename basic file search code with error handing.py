fname = input("Enter the file name: ") 
try: 
    fhand = open(fname)
    print("File can be opened")
except: 
    print("Error: file can not be opened, file name:", fname)
print("All done") 

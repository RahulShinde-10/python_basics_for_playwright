#file is a data stored in a storage device. A python program can talk to the file by reading content from it and write content to it

# type of files - text files (.txt) and binary files(.jpg)

#read files
#file = open("myfile.txt")
#readdata = file.read()
#print(readdata)
#file.close()


#write files
#file = open("myfile.txt", "w")      #you will open the file which you want to open along with operation as "w" or" "r"
#add = file.write("Hey shital")      # you will add the text in tha file which you want to add using .write
#file.close()                         # you will clos the file



# reading the lines from file
#file = open("myfile.txt")
#reading_the_lines = file.readlines()         # using .readlines you will printing the lines present in the file
#print(reading_the_lines)
#file.close()


# modes of opening a file
#r - read
#w - write
#a - append
#+ - updating
#rb - open for read in binary mode
#rt - open for read in text mode


#with statement
# best way to to open and close the file automatically is with statement
#with open ("myfile.txt") as file:
#    text = file.read()

#print(text)


#practice set
#finding the word is present in file or not
file = open("myfile.txt")
findword = file.read()
if ("shital" in findword):
    print("word is present")
else:
    print("word is not present")
file.close()

# Read the myfile.txt
read_file = "myFile.txt"
open_file = open(read_file, "r")


# Pint the file
fileContents = open_file.read()
print(fileContents)

# type of file
print(type(fileContents))

# Close the file
open_file.close()

# Using "with" is a better practice to open and close the file

with open(read_file, "r") as my_file:
    fileContents = my_file.read()
print("Reading file content using 'with: " + fileContents)

# reading specific characters from the file as:
with open(read_file, "r") as my_file:
    print("Read the first 5 characters: " + my_file.read(5))
    
# Read certain amount of characters
with open(read_file, "r") as my_file:
    print("Read 'Example': "+ my_file.read(7))
    print("Read 'of' in a new line: "+ my_file.read(3))
    print("Read 'reading' in a new line: "+ my_file.read(9))
    print("Read 'text': " + my_file.read(5))
    print("Read 'from' : " + my_file.read(4))
    print("Read 'file: '" + my_file.read(5))

#Read individual line in a file
with open(read_file, "r") as my_file:
    print("The first line in rea_file:" + my_file.readline())

#Loop through file contents/each line

with open(read_file, "r") as my_file:

    for line in my_file:
        print("Display all contents in my_file:" + str(line))
        
# Save the file as a list and display specific line in the file

with open(read_file, "r") as my_file:
    convert_to_list = my_file.readlines()  ## readlines() is a list while readline()is a single line
    print("Display the first line in conver_to_list file: "+ convert_to_list[0])
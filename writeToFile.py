# Writin to files

with open("PythonBasics\writeFile\writeFile.txt", "w") as write_to_file:
    write_to_file.write("Write first line to 'writeFile.txt'")

# Let verify if it's work by using read function

with open("PythonBasics\writeFile\writeFile.txt", "r") as test_write_file:
    print(test_write_file.read())

# Write multiple lines as follows:
with open("PythonBasics\writeFile\writeFile.txt", "w") as write_to_file:
    write_to_file.write("This be SECOND line\n")
    write_to_file.write("This should be THIRD line\n")

# Verify all text are written into our file
with open("PythonBasics\writeFile\writeFile.txt", "r") as test_write_file:
     print(test_write_file.read())

# Change the mode argument to append "a" work same as "w" mode
with open("PythonBasics\writeFile\writeFile.txt", "a") as write_to_file:
    write_to_file.write("Change the mode argument to 'a', which work same as mode 'w' argument")

# Verify new text in the file

with open("PythonBasics\writeFile\writeFile.txt", "r") as test_write_file:
    print(test_write_file.read())

# We can write list of items to writeFile.txt as follows:
with open("PythonBasics\writeFile\writeFile.txt","w") as write_to_file:
    write_to_file.write("Domestic animal\nWide animal\n")

#Verify list items in our file

with open("PythonBasics\writeFile\writeFile.txt", "r") as test_write_file:
    print(test_write_file.read())

print("____________________________________________________________________")

# Copy one file to other file

with open("PythonBasics/readFile/myFile.txt", "r") as read_file:

    """
        Copy details of myFile.txt and write it into writeFile.txt
     """
    with open("PythonBasics\writeFile\writeFile.txt", "w") as write_to_file:
        for line in read_file:
            print(line)
            write_to_file.write(line)

#Verify myFile.txt contents are copy into writeFile.txt

with open("PythonBasics\writeFile\writeFile.txt", "r") as test_write_file:
    print("Copy and write all the content from myFile.txt into writeFile.txt:\n"+test_write_file.read())

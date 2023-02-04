#!/usr/bin/python3

import os

#a function to creat a file in the current directory
def creatFile():

    #asking user for the filename
    filename = input("enter the filename: " )

    #creating the file using open
    with open(filename+".txt" , "w+") as f:
        
        #prompting for the files content
        message = input("what do you wish to save in the file: ")

        #writing to the new file
        f.write(message + "\n")

    #checking if the file was created
    if filename:
        print("file created successfully.","\nfilename: ",filename,"\nContent:")

        #opening the file to print its content
        f=open(filename +".txt", "r")
        for line in f:
            print(line)
        f.close
        
    #prints error messange if operation was unsuccessful    
    else:
        print("error creating file")


#a function to rename a file
def renameFile():
    #getting the old and new file names
    old_filename = input("Enter the name of the file you wish to rename: ")
    new_filename = input("Enter the new filename: ")

    try:
        #trying the renaming process
        os.rename(old_filename + ".txt" , new_filename + ".txt")
        print("File renamed Successfully!")

    except FileNotFoundError:
        #if the file does not exist
        print("File Not Found")


#a function that search for a file in the current directory
def searchFile():
    
    #asking the user for the files name
    file = input("Enter the file name: " )

    #checking if the file exists
    if file in os.listdir():

        #if found
        print("The File {} was Found".format(file))

    else:
        #if the file was not found 
        print("The file {} not Found".format(file))
  


#a function tha edits files in the current directory
def editFile():
    #asking the user for the file name
    filename = input("Enter the filename: ")

    #checking if the file exists
    if filename +".txt" in os.listdir():

        #if it does we open the file for writing
        with open(filename +".txt", "w") as f:

            #ask the user the updated message
            message = input("Enter the new content: ")

            #writing the new content to the file
            f.write(message + "\n")

        #reading the new content
        with open(filename + ".txt", "r") as f:
            print("Filename:", filename)
            print("Updated Content:")
            for line in f:
                print(line)

    else:
        #if the file does not exist
        print(f"the file '{filename}' was not Found.")


#a function that lists files in the current directory
def listFiles():
    #loops through the current directory and prints all the files
    print("Files in the current directory are:\n")
    for i,file in enumerate(os.listdir()):
        print(i,"-",file)
        print()




#a function to change current directory
def changeDirectory():

    #ask user for the new directory
    new_dir = input("Enter the new directory path: ")

    try:
        #try to change the current path
        os.chdir(new_dir)
        print("Directory Changed Successfully!")

        #print the new directory
        print("Current directory:", os.getcwd())

    except FileNotFoundError:
        #if the location/path nod found
        print("Directory not found")

#a function that prints the current working directory
def currentDirectory():
    print("Current Working Directory: ", os.getcwd())


#a function that deletes a file in the current directory
def deleteFile():
    #asking the user for the file name
    filename = input("Enter the file name: ")

    try:
        #deleting the file
        os.remove(filename + ".txt")
        print("File successfully deleted.")

    except:
        #if the file is not found
        print("Error: File cannot be deleted or Not Found.")




#a function to read a file
def readFile():
    #getting filename from the user
    filename = input("Enter the file name: ")

    try:
        #trying to open th file
        with open(filename + ".txt", "r") as f:

            #reading files content
            content = f.read()

            #displaying files content
            print()
            print("File Contents:>> ",end="")
            print(f"' {content} '")

    except FileNotFoundError:
        #if the file is not found
        print("Error: File Not Found.")


while(True):

    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("Welcome to Simple file Manager by Freedom469")
    print("_______________________________________________")
    print()
    option = input("""
        With this programe you can:

        1:>> Creat a File.

        2:>> Edit a File.

        3:>> Delete a File.

        4:>> Search for a file.

        5:>> List All Files.
        
        6:>> Change Directory.

        7:>> Show Current Directory.

        8:>> Rename File.

        9:>> Read File.

        0:>> Exit.


________________________________________________________

        """
        )

    options =  ["0","1","2","3","4","5","6","7","8","9"]
    if option in options:
    
        if option == "1":
            print("________________________________________________")
            print()
            creatFile()

        elif option == "2":
            print("________________________________________________")
            print()
            editFile()

        elif option == "3":
            print("________________________________________________")
            print()
            deleteFile()

        elif option == "4":
            print("__________________________________________________")
            print()
            searchFile()

        elif option == "5":
            print("____________________________________________________")
            print()
            listFiles()
            print()

        elif option == "6":
            print("____________________________________________________")
            print()
            changeDirectory()
            print()

        elif option == "7":
            print("____________________________________________________")
            print()
            currentDirectory()
            print()

        elif option == "8":
            print("____________________________________________________")
            print()
            renameFile()
            print()

        elif option == "9":
            print("___________________________________________________")
            print()
            readFile()
            print()

        elif option == "0":
            exit(0)


    else:
        print("Invalid Option. Exiting..")
        exit(-1)

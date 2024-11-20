def read_file(file):
    openFile=open(file)
    readFile=openFile.read()
    return readFile

def modify_file(readFile):
    modifiedFile=readFile.upper()
    return modifiedFile
def new_modified_file(modifiedFile,newFile):
    openNewFile=open(newFile,'w')
    writeFile=openNewFile.write(modifiedFile)
    return writeFile

file = input('Enter the file name: ')
try:
    content = read_file(file)
    modified_content = modify_file(content)
    
    newFile = input('Enter the new file name to save modified content: ')
    new_modified_file(modified_content, newFile)
    print(f"Modified content has been saved to {newFile}")
except FileNotFoundError:
    print(f"The file {file} was not found. Please check the file name and try again.")
except PermissionError:
        print(f"Error: Permission denied to read the file '{file}'.")
except IOError:
        print(f"Error: There was an I/O error while trying to read the file '{file}'.")
except UnicodeDecodeError:
        print(f"Error: The file '{file}' contains non-text data and cannot be read as a text file.")
    
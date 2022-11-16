import os
import string
import random

# creates empty arrays
files = []
changedfiles = []

# selecting option
option1 = int(input("Only files (1) or everything (2): "))


# function for generating random names
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# checking all files in dir and appending in "files" array, only files or files + dir depends on option you selected
for file in os.listdir():
    if option1 == 1:
        if os.path.isfile(file):
            files.append(file)
    else:
        files.append(file)


# printing all files are about to change names
print("files to change: ", files)


# changing files names
for file in files:
    # slpliting file names to base and extension
    filebase = os.path.splitext(file)[0]
    fileext = os.path.splitext(file)[1]

    # checking length of files
    filelen = len(file)

    newname = id_generator(filelen)     # randomize new names
    newnameext = newname + fileext      # combining changed files name and its old extension
    os.rename(file, newnameext)         # renaming files
    changedfiles.append(newnameext)     # appending changed files names to "changedfiles" array

print("Your files changed names for: ", changedfiles)   # listing all changed file names
input()     # waiting for input to end program

# KC 13/02/2021

import csv
letters = ["A", "B", "C", "D", "E"] # Alphabet because I forget a lot
types = ["front", "rear", "drag"] # For the different maps

for letter in letters:
    filename = "aero"+letter # Put in aero name here

    file = open(filename+".txt", "r")

    # Value initilisation
    zValues = [0, 0, 25, 50, 75, 100] # Always the same so no point extracting them
    startLine = 38
    endLine = 43
    fileReader = file.readlines()

    for i in range(3): # For the 3 important batches of data

        xyValues = []  # Soon to be 2D array holding all lines from batches of data
        for j in range(startLine, endLine):

            currentLine = fileReader[j].split("\t") # Splits the values by the /t that is used to seperate them

            # Some files don't have the /n annoyingly
            try:
                del currentLine[6]  # Removes an annoying /n
            except:
                print("No annoying /n found!")

            for q in range(0, 6):
                currentLine[q] = int(currentLine[q]) # Casts the elements so that they are all integers
            xyValues.append(currentLine)

        with open(filename + types[i] + ".csv", "w", newline="") as writeFile:
            writer = csv.writer(writeFile)
            headerline = 0  # Just a line counter
            for z in xyValues:
                writer.writerow(z) # Writes the actual FRH and downforce/drag values

        writeFile.close()

        # Each new batch of data is 16 lines apart
        startLine += 16
        endLine += 16
        
    file.close()





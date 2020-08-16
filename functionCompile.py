# mcfunction "compiler" that lets you use nice things
# because mcfunctions are painful to work with
# 16/07/2020
# (C) 2020 AdamantPenguin
##############################################################
# some options here
ifKeyword = "if"
beginIfKeyword = "{"
endIfKeyword = "}"
executeCommandStart = "execute"
executeCommandEnd = "run"
##############################################################
import os

inputFile = input("Please enter the input file path: ")
outputFile = input("Please enter the output file path: ")
executeParams = []

fIn = open(inputFile)
fOut = open(outputFile, "a")
fOut.write("aaa") #     make sure the file exists
fOut.close()
os.remove(outputFile) # because now it doesn't
fOut = open(outputFile, "a")

for line in fIn: # for each line in the file
    stripped = line.strip() # take all whitespace off the start and end
    if stripped.find(ifKeyword) == 0: # if this is an if statement
        # find the execute parameters and put them in the list
        executeParams.append("if " + stripped[len(ifKeyword) + 1:-1 - len(beginIfKeyword)])
    elif stripped.find(endIfKeyword) == 0: # if this is the end of an if statement
        del executeParams[-1] # remove the most recent execute parameter
    else:
        if len(executeParams) == 0:
            fOut.write(stripped + "\n")
        else:
            # build up the execute command
            executeCommand = executeCommandStart + " "
            for param in executeParams:
                executeCommand = executeCommand + param + " "
            executeCommand = executeCommand + executeCommandEnd
            fOut.write(executeCommand + " " + stripped + "\n")

fOut.close()
fIn.close()

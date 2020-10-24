import sys

for inputString in sys.stdin:
        outputString = inputString[0]
        for i, char in enumerate(inputString):
                if (char == "-"):
                        outputString += inputString[i+1]
        print(outputString)
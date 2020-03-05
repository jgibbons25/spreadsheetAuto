import re #regular expressions
import os #to handle file paths for different operating systems
import fileinput

os.chdir('./') #change functioning directory to the folder of this file

def formatName(name):
    name = str(name)
    if len(name) >= 2:
        name = name[0] + name[1:].lower() #keep first letter capitalized
        name = name
    return name

def bashPause():
    try:
        programPause = raw_input("Press the <ENTER> key to continue...")
    except:
        programPause = input("Press the <ENTER> key to continue...")

def makeNewFile():
    global fileNameInput, newFile, sceneNum, rowName
    print('Starting file with scene number ' + str(sceneNum))
    try:
        newFile.close()
    except:
        pass
    
    if len(fileNameInput) > 4 and fileNameInput[0:5] == "Scene":
        newFileName = fileNameInput + '.csv'
    else:
        newFileName = 'Scene' + str(sceneNum) + '_' + fileNameInput + '.csv'
    newFile = open(newFileName, 'w')
    #first line of the file should contain column names
    newFile.write(',Speaker,Expression,Sound,Text,SpecialEvent,SpecialEffect,CharX,CharY,CharScale\n')
    rowName = 1
    sceneNum += 1


fileFound = False

while not fileFound:
    print("What is the file name (no file extension needed)?")
    try:
        fileNameInput = input()
    except:
        fileNameInput = raw_input()
    fileName = fileNameInput + ".txt"
    fileFound = os.path.isfile(fileName)
    if not fileFound:
        print("ERROR: Cannot find a .txt file in this folder with that name. Please try again."
              "\n***"
              )


print("What's the first scene number?")
try:
   sceneNum = int(input())
except ValueError:
    print("That wasn't a valid number. Defaulting to scene number 0.")
    sceneNum = 0

scriptFile = open(fileName) #w opens in write mode
fullScript = scriptFile.readlines()
scriptFile.close()

makeNewFile()

print("Start at what row number?")
try:
    rowName = int(input())
except ValueError:
    print("That wasn't a valid number. Defaulting to row number 1.")
    rowName = 1


#loop through each line, alter it, and write it to new file
for line in fullScript:
    line = line.rstrip('\n')
    line = line.replace('"', '""') #exit out of double quotes by making two
    name = dialogue = specialEvent = '' #reset vars in the loop
    if len(line) >= 1:
        if line[0] != "#":  #hashtags reserved for comments
            if line[0:2] == "__":
                makeNewFile()
            elif line[0] == '*':
                try:
                    specialEvent, dialogue = line.split(': ', 1)
                except:
                    #if no colon, just set the special event
                    specialEvent = line
                specialEvent = specialEvent[1:] #take out asterisk
                
            else:
                try:
                    name, dialogue = line.split(': ', 1) #split line only once
                    name = formatName(name)
                except:
                    print("This string could not be split:")
                    print(line)
                    name = line


    line = str(rowName) + ',"' + name + '","Nothing","None","' + dialogue + '","' + specialEvent + '","none","0.0","0.0","0.0"\n'
    
    newFile.write(line)
    rowName += 1


newFile.close()
print("Script conversions complete!")
bashPause()

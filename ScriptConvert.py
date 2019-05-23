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

def makeNewFile():
    global fileNameInput, newFile, sceneNum, rowName
    print('Starting file with scene number ' + str(sceneNum))
    try:
        newFile.close()
    except:
        pass
    newFileName = 'Scene' + str(sceneNum) + '_' + fileNameInput + '.csv'
    newFile = open(newFileName, 'w')
    #first line of the file should contain column names
    newFile.write(',Speaker,Expression,Sound,Text,SpecialEvent,SpecialEffect,CharHorizontal,CharScale\n')
    rowName = 1
    sceneNum += 1


fileFound = False

while not fileFound:
    print("What is the file name (no file extension needed)?")
    fileNameInput = input()
    fileName = fileNameInput + ".txt"
    fileFound = os.path.isfile(fileName)
    if not fileFound:
        print("ERROR: Cannot find a .txt file in this folder with that name. Please try again."
              "\n***"
              )

    
print("What's the first scene number?")
sceneNum = int(input())

scriptFile = open(fileName) #w opens in write mode
fullScript = scriptFile.readlines()
scriptFile.close()



rowName = 1
makeNewFile()


#loop through each line, alter it, and write it to new file
for line in fullScript:
    line = line.rstrip('\n')
    line = line.replace('"', '') #quotation marks cause error
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


    line = str(rowName) + ',' + name + ',Nothing,,"' + dialogue + '",' + specialEvent + ',,,\n'
    
    newFile.write(line)
    rowName += 1


newFile.close()
print("Script conversions complete!")


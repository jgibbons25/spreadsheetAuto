This Python script is designed to convert dialogue scripts in .txt format to a .csv compatible with the VN Framework. Dialogue files should have the following format (comments are after the # symbol):

______
# To separate scenes into new files, put a line with at least one underscore between each scene.
NAME: Dialogue. 
NAME2: More dialogue. 
# The script will look for the colon and separate the name from the dialogue accordingly.
# Comments can be on their own line with a hashtag symbol
# SpecialEvent commands can be added after a * symbol. These don't work perfectly; you'll usually need to clean up the Special Events more later. But they can be useful as such:
NAME: I have a choice to make!
*ChoiceA: Yes
*ChoiceB: No
*ChoiceAStart
NAME: Here's the branch for ChoiceA!

#IMPORTANT NOTE: any double-quotes in your text (") will be stripped out of the file. Otherwise, they cause errors
______

HOW TO RUN THE SCRIPT:
1) Save your full dialogue file as a .txt
2) Put ScriptConvert.py file in the same folder as the .txt file containing your dialogue script.
3) Make sure you have Python 3 downloaded on your computer. You can download it here: https://www.python.org/downloads/release/python-373/ Make sure you install it to show up in your Start Menu
4) Open Python Idle GUI (should be available in the Start Menu after installing Python)
5) From Python Idle, go to File > Open. Browse to the location of the ScriptConvert.py file.  
6) From the ScriptConvert.py opened file, press F5. This will start the conversion process. Answer the questions in the Idle window to finish conversion


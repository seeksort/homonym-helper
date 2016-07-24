### Homonym Helper ###
'''
This program will open a file, look for instances of 
either: (1) there / their / they're [ttt] or (2) your / 
you're [yy] (it will ask if you want to search for one or 
both), search the file, present each instance of the 
word in context, and ask if you want to replace the 
word with one of the available homophones for that word.
'''
import os

# Small dictionary for now.
homonymsDict = {1 : ["there", "their", "they\'re"], 2: ["you're", "your"]}

### 1. Open file ###
'''
- Greeting message
- Check if current working directory is ok or if user
wants another file path
	- Request file path
	- *Throw errors if invalid file path
- Request file name via input
	- Success message
	- *Throw errors if cannot open file / does not exist
'''
print ("------------------------------------------")
print ("~*~*~*~ Welcome to Homonym Helper! ~*~*~*~")
print ("------------------------------------------")
print ("ver. 0.01")
print ("")
print ("This program will help you make sure you're not using homonyms incorrectly!")
print ("")
print ("Currently, I can help you with finding and replacing instances of the following in a file: \n\n\"there / their / they're\" \nand \n\"your / you're\"\n")

def validatePath(path):
	'''
	Validate that user-defined path is an actual path on
	the computer.
	'''
	try:
		currentPath = os.chdir(path)
	except FileNotFoundError:
		print("\nThis is not a valid directory. Please try again.")

def confirmDesiredPath(currentPath):
	'''
	Check the current working directory and ask if the
	user wants to use the current path or input a different
	path.
	'''
	while True:
		currentPath = os.getcwd()
		print("Your current directory is: ")
		print(currentPath)
		userResp = input("Do you want to check a file in this directory? (Y/N) \n")
		if userResp == "Y":
			return currentPath
		elif userResp == "N":
			currentPath = input("Please enter a path to search. \n")
			validatePath(currentPath)
		else:
			print("Please enter a valid response.")

def requestFileName():
	'''
	Asks user to input file name in current directory.
	'''
	fileName = input("Please enter the name of the file: \n")
	return fileName

def openValidateFile(path):
	'''
	Concatenates path and file name and tries to open address.
	Throws an exception if operation fails, throws a high
	five if it succeeds.
	'''
	while True:
		fileName = requestFileName()
		address = path + "/" + fileName
		try:
			fileToReview = open(address)
			print("File opening was succeessful.")
			return fileToReview
		except FileNotFoundError:
			print("This is not a valid file in this directory. Please try again.")

### 2. Request homonym to check ### 
#TODO (in progress)
'''
- Request word via input
- Validate that word is:
	- a homonym
	- not less than one character (potentially useful in future)
'''
def requestUserWord():
	'''
	Asks user to input word.
	'''
	userWord = input("Please enter the homonym you would like to check: \n")
	return userWord

def validateHomonym():
	'''
	Tries to match provided word to program's homonyms dictionary.
	'''
	while True:
		word = requestUserWord()
		for key in homonymsDict.keys():
			if word in homonymsDict[key]:
				homonymsToSearch = homonymsDict[key]
				print("word success!") #debug
				return homonymsToSearch
			else:
				print("That is not in our homonyms dictionary.")

'''
## TODO ##
3. Scan file
	+ Return: no matches found
	+ Return: each match, go to 4
4. Display each match in context (5 words before & after), request user to confirm or change word
5. If changed, display change in context before changing in file ("This sentence has not yet been changed. Please confirm change below.")
6. If approved, change text fragment, if not, move on
7. Save copy of file.
'''


currentPath = os.getcwd()
filePath = confirmDesiredPath(currentPath)
print("filePath is: " + filePath) #debug
fileToReview = openValidateFile(filePath)
readFile = fileToReview.read()
print("File contents are below:\n")
print(readFile) #debug
validateHomonym()














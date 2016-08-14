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
print ("This program will help you make sure you're using homonyms correctly!")
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
		userResp = input("Do you want to check a file in this directory? (Y/N) \n(press ctrl+c to quit) \n>>").upper()
		if userResp == "Y":
			return currentPath
		elif userResp == "N":
			currentPath = input("Please enter a path to search. \n(press ctrl+c to quit) \n>>")
			validatePath(currentPath)
		else:
			print("Please enter a valid response.")

def requestFileName():
	'''
	Asks user to input file name in current directory.
	'''
	fileName = input("Please enter the name of the file (press ctrl+c to quit): \n>>")
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
			print("This is not a valid file in this directory. Please try this program again.\n")

### 2. Request homonym to check ### 
#TODO (in progress)
'''
- Request word via input
- Validate that word is:
	- a homonym
	- not less than one character (potentially useful in future)
'''
def requestUserHomonym():
	'''
	Asks user to select from list of homonyms
	1. there / their / they're
	2. your / you're
	'''
	while True:
		userWord = input("Please enter the # of the homonym list you would like to check: \n 1. there / their / they're \n 2. your / you're \n>>")
		if userWord == "1":
			userWord = ["there", "their", "they're"]
			return userWord
		elif userWord == "2":
			userWord = ["your", "you're"]
			return userWord
		else:
			print("That is not one of the options.")

### 3. Scan file ###
'''
- Split file into list
- Scan list for instances of words in the list
- Return 4 words before and 4 words after
- Return: no matches found
- Return: each match, go to 4
'''
def validateforHomonym(textFragment, homonymlist):
	for homonym in homonymlist:
		textFragmentList = textFragment.split()
		if len(textFragmentList) > 6:
			if homonym in textFragmentList[3].lower():
				print(homonymlist)
				print("homonym:" + homonym)
				print(textFragment)
				print(textFragmentList)
				print("success?")
				

def textFragmentDisplay(list, num):
	if num < 4:
		fragmentList = list[0:num+3]
	else:
		fragmentList = list[num-4:num+3]
	textFragment = " ".join(fragmentList)
	return textFragment

def compareHomonymToText(fileText, homonymlist):
	textList = fileText.split()
	counter = 0
	while counter < len(textList):
		textFragment = textFragmentDisplay(textList, counter)
		validateforHomonym(textFragment, homonymlist)
		#print(counter)
		counter += 1
	print(textList)
'''
## TODO ##
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
wordsToCheck = requestUserHomonym()
compareHomonymToText(readFile, wordsToCheck)












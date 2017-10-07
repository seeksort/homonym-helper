### Homonym Helper ###
'''
This program will open a file, look for instances of
either: (1) there / their / they're [ttt] or (2) your /
you're [yy] (it will ask if you want to search for one or
both), search the file, present each instance of the
word in context, and ask if you want to replace the
word with one of the available homophones for that word.
'''
import argparse
import os
import sys


parser = argparse.ArgumentParser(description='Presents homonyms in a text and '
											 'will ask if you meant to use '
											 'that word.')
parser.add_argument('--i',
                    help='The file path to the input file.',
					required=True)
parser.add_argument('--o',
                    help='The file path to the output file.',
					required=True)

args = parser.parse_args()
input_path = args.i
output_path = args.o


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
print ("ver. 0.01\n")
print ("This program will help you make sure you're using homonyms correctly!\n")
print ("Currently, I can help you with finding and replacing instances of the following in a file: \n\n\"there / their / they're\" \nand \n\"your / you're\"\n")


def confirm_desired_path(input_path):
	''' Check the current working directory and ask if the user wants to use the
		current path or input a different path.
	'''
	while True:
		print("Your current input file path is {0}".format(input_path))
		userResp = str(raw_input("Is this correct? (Y/N) \n(press ctrl+c to quit) \n>>")).upper()
		if userResp == "Y":
			return input_path
		elif userResp == "N":
			current_path = str(raw_input("Please enter the correct file path. \n(press ctrl+c to quit) \n>>"))
			return confirm_desired_path(current_path)
		else:
			print("Please enter a valid response.")


def open_validate_file(input_path):
	''' Concatenates path and file name and tries to open address. Throws an
		exception if operation fails, throws a high five if it succeeds.
	'''
	while True:
		try:
			file_obj = open(input_path)
			print("File opening was succeessful.")
			return file_obj
		except IOError:
			print("This is not a valid file. Please try this program again.\n")
			sys.exit()


### 2. Request homonym to check ###
#TODO (in progress)
'''
- Request word via input
- Validate that word is:
	- a homonym
	- not less than one character (potentially useful in future)
'''
def request_user_homonym():
	''' Asks user to select from list of homonyms.

		1. there / their / they're
		2. your / you're
	'''
	while True:
		selection = str(input("Please enter the # of the homonym list you would like "
						 "to check: \n 1. there / their / they're \n 2. your / "
						 "you're \n>>"))
		if selection == "1":
			return ["there", "their", "they're"]
		elif selection == "2":
			return ["your", "you're"]
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


def text_fragment_display(list, num):
	if num < 4:
		fragmentList = list[0:num+3]
	else:
		fragmentList = list[num-4:num+3]
	textFragment = " ".join(fragmentList)
	return textFragment


def compare_homonym_to_text(fileText, homonymlist):
	textList = fileText.split()
	counter = 0
	while counter < len(textList):
		textFragment = text_fragment_display(textList, counter)
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


file_path = confirm_desired_path(input_path)
file_to_review = open_validate_file(file_path)
read_file = file_to_review.read()
print("File contents are below:\n")
print(read_file) #debug
words_to_check = request_user_homonym()
compare_homonym_to_text(read_file, words_to_check)
file_to_review.close()

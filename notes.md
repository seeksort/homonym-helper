Notes for Spell Helper
======================

1. Open file
	+ Error: invalid file path
	+ Error: cannot open file
	+ Error: file does not exist
2. Request homonym to check
	+ Error: word less than one character
	+ Error: word not a homonym
3. Scan file
	+ Return: no matches found
	+ Return: each match, go to 4
4. Display each match in context (5 words before & after), request user to confirm or change word
5. If changed, display change in context before changing in file ("This sentence has not yet been changed. Please confirm change below.")
6. If approved, change text fragment, if not, move on
7. Save copy of file.

Ideas for Future Functionality
==============================
	+ Use a full homonym dictionary
	+ Write to actual file
	+ Write to Word docs
	+ Write to OpenOffice, LibreOffice, etc. docs
	
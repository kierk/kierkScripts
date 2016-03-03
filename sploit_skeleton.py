#! /usr/bin/env python

################################
#	Exploit Skeleton 
#	Black Hat Python Based
#	by kierk
#	
#	Usage: python sploit_skeleton.py [-l ]
################################

################################
#	Contents:
#		+ Example:varNameForGrab
#
#
#
#
#
#		+ Building Blocks:EOF
#			- replace(file, searchTxt, replaceTxt) - find and replace
#			- yesno("\nQUESTION? [y/n] ") - handler for yes no questions
#
################################

################################
# ToDo:
#	-Update Line numbers
#	-Add direct write functionality
################################



################################
#
#
#
################################



################################
#
#
#
################################



################################
#	Basic Blocks:
#		-General Copy Pasta
################################

# Find and Replace text in a file
import fileinput
def replace(fileToSearch, textToSearch, textToReplace):
	file = fileinput.FileInput(fileToSearch, inplace=True)
	for line in file:
		print line.replace(textToSearch, textToReplace),

# Usage: answer = yesno("\nWould you like a bannana? [y/n] ")
def yesno(prompt, retries=4, complaint='Reply yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes', 'Yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope', 'No'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

def printHead():
	print '''#! /usr/bin/env python

################################
#       Exploit Skeleton
#       Black Hat Python Based
#       by kierk
#
################################


'''

def printMain():
	print '''

# Main to Edit
def main():
	pass


if __name__ == "__main__":
    main()


################################ END OF FILE

'''


# Main syntax for python flo
def main():
	printHead() #prints info header

	# Add Flag Handling for Functions Here:

	printMain() #prints main
	pass

if __name__ == "__main__":
    main()


################################ END OF FILE

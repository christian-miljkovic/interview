"""
Challenge Details
Assume you are designing a performance application to match keywords found in a url. 
What data structures / technologies would you employ to ensure a speedy (sub 10ns) algorithm that is able to match substrings against the URL?
To help shape your thinking, let's assume that we're dealing with a finite subset of words. 
This may help bound which algorithms would be most applicable for this problem. 
"""

# Do a naive search but then cacluate how much you jump if you do not have a find
# pre calculate the key words in a hash table so if you had hello -> h, he, hel, hell, hello for 
# quick comparisons 

"""
python -m cProfile -s cumtime urlSubStringFinder.py
{'python': [12, 35], 'documenting': [23]}
         57 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 urlSubStringFinder.py:7(<module>)
        1    0.000    0.000    0.000    0.000 urlSubStringFinder.py:59(findSubString)
       50    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 urlSubStringFinder.py:32(preCalculateHash)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {len}

"""


def preCalculateHash(*patterns):
	"""
	Parameters
	-----------
	pattern: str 
		the key word that we are going to search the in the url

	Returns
	-------
	dict
		dictionary representing a hash_table for each substring of the pattern

	"""
	hash_table = dict()
	

	for string in patterns:
		subString = ""
		for char in string:
			subString += char
			hash_table[subString] = True
		# So that we can recognize the end of the string
		hash_table[subString] = '*'

	return hash_table


def findSubString(urlText, *keyWords):

	if len(urlText) > 1:

		startingIndex = dict()

		hash_table = preCalculateHash(*keyWords)
		i = 0
		j = 0
		subString = ""
		length = len(urlText)

		while j < length:
			subString += urlText[j]

			if subString in hash_table.keys():

				if hash_table[subString] == '*':

					# This is in the case there are multiple strings that match the pattern
					if subString in startingIndex.keys():
						startingIndex[subString].append(i)
					else:
						startingIndex[subString] = [i]

					j += 1
					i = j
					subString = ""
				else:
					j += 1
			else:
				j += 1
				i = j
				subString = ""

		return startingIndex		

if __name__ == "__main__":
	print(findSubString('https://realpython.com/documenting-python-code/','python','documenting'))






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
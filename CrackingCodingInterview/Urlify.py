"""
Chapter 1 Array's and Strings URLify problem
Write a method to replace all spaces in a string with '%20'. You may assum that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
"""

def urlIfy(strToUrl):

    str_list = strToUrl.split()
    ret_str = ""
    for i in range(0, len(str_list) - 1):
        ret_str += str_list[i] + "%20"
    ret_str += str_list[len(str_list) - 1]
    return ret_str

if __name__ == "__main__":
    str_input = "Mr John Smith   "
    print(urlIfy(str_input))
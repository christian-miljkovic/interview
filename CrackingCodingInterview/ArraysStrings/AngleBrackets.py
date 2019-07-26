"""
Given a string of brackets, add '<' or '>' to the string to properly close 
the entire nested set of brackets.

Example
Input: <<><<> 
Output: <<>><<>>

"""


def solution(angles):
    
    if len(angles) == 0:
        return angles
    
    if len(angles) == 1:
        return singleSet(angles)
    else:
        
        split_index = []
        bracket_array = []
        i = 1
        j = 0

        while i != len(angles) - 1:
            if angles[j] + angles[i] == '><':
                split_index.append(j)
            i += 1
            j += 1
        
        if len(split_index) > 0:
            angle_list = construct_list(split_index, angles)
            for index, ele in enumerate(angle_list):
                angle_list[index] = singleSet(ele)
            return ''.join(angle_list)
        
        else:
            return singleSet(angles)
        

def construct_list(indicies, angles):
    
    angle_list = []
    
    if len(indicies) == 0:
        return None
    if len(indicies) == 1:
        index = indicies[0] + 1
        angle_list.append(angles[:index])
        angle_list.append(angles[index:])

    else:
        i = 0
        j = -1
        while i != len(angles) - 1:
            if j == -1:
                angle_list.append(angles[:indicies[i]])
            else:
                angle_list.append(angles[indicies[j]:indicies[i]])
            
            j += 1
            i +=1
        
        if indicies[j] != len(angles) - 1:
            angle_list.append(angles[indicies[j]:])
            
            
    if "" in angle_list:
        return angle_list.remove("")
    else:
        return angle_list

    
def singleSet(angles):

    totalBrackets = 0
    if angles[0] == '>':
        angles = '<' + angles

    for char in angles:
        if char == '<':
            totalBrackets -= 1
        else:
            totalBrackets += 1
    
    bracket_list = []
    
    if totalBrackets < 0:
        for i in range(abs(totalBrackets)):
            bracket_list.append('>')
        brkStr = ''.join(bracket_list)
        return angles + brkStr
        
    elif totalBrackets > 0:
        for i in range(totalBrackets):
            bracket_list.append('<')
        brkStr = ''.join(bracket_list)
        return brkStr + angles
    else: 
        return angles
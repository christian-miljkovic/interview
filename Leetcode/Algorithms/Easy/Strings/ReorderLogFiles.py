"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""

"""
Input: list of {logs} -> logs = <alphanum_id> lower_chars or digits
letter_logs = <alphanum_id> + lower_chars
digit_logs = <alphanum_id> + digits

Edge Cases:
- leter log the same therefore have to sort by id
- logs == 0




Output: first letterlogs then digit logs
- Sorted letterlogs ignoring id unless tie, original order of digit logs


"""

# Cleaner refactored code
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        if not logs:
            return []
        
        alpha_logs, digit_logs = split_log_types(logs)
        
        sorted_alpha_logs = sorted(alpha_logs, key=lambda x: (x[1],x[0]))
        full_list = [x[0] + " " + x[1] for x in sorted_alpha_logs]
        full_list.extend(digit_logs)
        
        return full_list
        
        
        
def split_log_types(logs):
    
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        alnum, trailing_log = log.split(' ', 1)
        if trailing_log[-1].isalpha():
            letter_logs.append((alnum, trailing_log))
        else:
            digit_logs.append(log)
    
    return letter_logs, digit_logs
        



# Time Complexity: O(nm) where n is the size of the logs list, and m is the size of the largest str log
# Space Complexity: O(n)
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs, digit_logs = process_logs(logs)
        sorted_letter_logs = sorted(letter_logs,key=lambda x: (x[1],x[0]))
        clean_letter_logs = [' '.join(log) for log in sorted_letter_logs]
        clean_letter_logs.extend(digit_logs)
        
        return clean_letter_logs
        
        
        
def process_logs(logs):
    
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        _id, _msg = log.split(" ",1)

        if _msg.replace(" ","").isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append((_id,_msg))
            
    return letter_logs, digit_logs
"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""

# Functioning solution:

class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            # if the id is alpha numeric then return (0, rest, id_) otherwise (1,) which will automatically just put
            # the numeric ids behind in order since it will not sort based on rest and id
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)


# NOT FUNCTIONING DUE TO IMPROPER SORT METHOD
def seperateLogs(logs):

    digit_logs = []
    alpha_logs = []

    for log in logs:
        if str.isdigit(log[-1]) == True:
            digit_logs.append(log)
        else:
            alpha_logs.append(log)

    return (alpha_logs, digit_logs)

def compareLogs(log_A, log_B):
    log_split_A = log_A[i].split()
    words_A = ''.join(word for word in log_split_A[1:])

    log_split_B = log_B[i].split()
    words_B = ''.join(word for word in log_split_B[1:])

    if words_A < words_B:
        return -1
    elif words_A > words_B:
        return 1
    else:
        return 0

def sortAlphaLogs(logs):

    sorted(logs, key=compareLogs)
    return logs
                


class Solution:
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        alpha_logs, digit_logs = seperateLogs(logs)
        alpha_logs = sortAlphaLogs(alpha_logs)
        
        alpha_logs.extend(digit_logs)
        return alpha_logs
        
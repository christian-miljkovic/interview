"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.

"""

"""
Inputs: emails -> each email contains @, local/domain != "", local[0] != +
only contains alphabetical or + or .

ex: a.b@gmail.com == ab@gmail.com

Output: Number of unique emails

Edge cases: local[0] == '.', domain contains multiple '.', domain can contain +

Algorithm:
1. Loop through each email
2. Pop the elements before @
3. "Clean" the local name based upon the above criteria
4. Do hash_map[domain] = [local1]
5. If domain is there then add new local email
6. Loop through hash_map and count the length of each list in for each key add this to total

Time Complexity: O(n*m)
Space Complexity: O(n)

Improvement: Could use a set instead of a hash_map and add the canonical email
which means the cleaned email including the domain. Sets don't allow you to add
the same values and don't give you an error if you try to do so.

"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        hash_map = dict()
        for email in emails:
            local, domain = email.split("@",1)
            cleaned_local = clean_local(local)
            if domain not in hash_map:
                hash_map[domain] = [cleaned_local]
            else:
                if cleaned_local not in hash_map[domain]:
                    hash_map[domain].append(cleaned_local)
        
        total_emails = 0
        for key, val in hash_map.items():
            total_emails += len(val)
        
        
        return total_emails
            
def clean_local(local_str):
    
    return_list = []
    for char in local_str:
        if char == '+':
            break
        elif char != '.':
            return_list.append(char)
    
    return ''.join(return_list)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
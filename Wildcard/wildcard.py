"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

"""


def ismatch (s: str,p: str):
    if len(s) != len(p) and '*' not in p:
        return False 
    elif '*' in p and len(p) == 1:
        return True

    else:
        i = 0
        while i < len(s):
            if s[i] != p[i] and p[i] != "?":
                return False
            i += 1
    return True

print(ismatch("aa","a"))
    

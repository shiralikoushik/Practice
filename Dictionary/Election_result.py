""" 
Dictionary and counter in Python to find winner of election

Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.
Examples: 
Input :  votes[] = {"john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"};
Output : John
We have four Candidates with name as 'John', 
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.

"""


input1 = [
    "john",
    "johnny",
    "jackie",
    "johnny",
    "john",
    "jackie",
    "jamie",
    "jamie",
    "john",
    "johnny",
    "jamie",
    "johnny",
    "john",
    "meg",
    "meg",
    "meg",
    "meg",
    "megha",
    "aaa",
    "aaa",
    "aaa",
    "aaa",
    "aa",
    "aa",
    "aa",
    "aa",
]
t_set = set(input1)
# print(t_set)
dict1 = {i: input1.count(i) for i in t_set}
max_val = max(dict1.values())

max_lt = [(val, ky) for ky, val in dict1.items() if val == max_val]

print(min(max_lt)[1])

# date : 13/11/2020
# Author : Renato Gusani
# Student no. : x19411076
# Question : 3a

# a)
import re
pat = "[a-zA-Z0-9]"
user_input = input("Input Regex:")
if (re.search(pat, user_input)):
    print ("True")
else:
    print("False")

# b)
# function to highlight words
import re
def re_show(pat, s):
    print(re.compile(pat, re.M).sub("{\g<0>}", s.rstrip()))

# paragraph as used in question
s = """Betty Botter bought a bit of butter
But, she said, this butter’s bitter
If I put it in my batter
It will make my batter bitter
But a bit of better butter
Will make my batter better
So ’twas better Betty Botter bought a bit of better butter"""


# ‘$’ matches the end of a line
re_show(r"butter$", s)
re_show(r"batter$", s)
re_show(r"better$", s)
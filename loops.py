""" For loops!
Here are some examples:
for x in "word":
  print(x)
OUTPUT: 
w
o
r
d
We can do this also with "for i" and with any letter we want 
explanation of for loop:
for x in "word": -> For every letter/character in the "word"
  print(x) -> We print the x  
"""
answer = input('Type a word(without a space) ') # The input
count = 0 # Count is 0
for x in answer: # for every character/letter in the answer
    count += 1 #  we add + 1 in the count for every character (test has 4 letters so it would return 4) 
    print(f"{x} -> {count}") # print every character and then the count

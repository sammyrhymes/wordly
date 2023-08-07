# read input from user
letters = input("Please input the letters separated by commas(,): ")
# # store in a list
letters = letters.split(',')
# # print(letters)

# words

words = ['app', 'eat', 'screnvmefnusdj']

# # iterate through it finding only those that are present
lst=[]
for word in words:
    #  use this as flag
    is_present = True
    for letter in letters:
        if letter not in word:
            is_present = False
    if is_present:
        lst.append(word)
# 
print(lst)
# # output the data
# hand = open('README.md')
# print(hand)
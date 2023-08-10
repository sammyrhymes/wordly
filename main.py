# read input from user
def readInput():
    inputLetters = input("Please input the letters:").strip(' ').lower()

    # store in a list
    letters = []
    for letter in inputLetters:
        letters.append(letter)

    return letters


# Get words
def readfromFile():
    fhand = open('words.txt')
    words = []

    for line in fhand:
        word = line.strip('\n')
        words.append(word)

    return words


# # iterate through it finding only those that are present
def findWords(words, letters):
    lst = []

    for word in words:
        if len(word) < len(letters)+1:

            #  use this as flag
            is_present = True

            for letter in letters:
                if letter not in word:
                    is_present = False

            if is_present:
                lst.append(word)
    return lst


# printing the output
def output(lst):
    count = 0

    if len(lst) < 1:
        print(f'No words found')

    for l in lst:
        print(f'{count} : {l}')
        count += 1

if  __name__ == '__main__':
    output(findWords(readfromFile(), readInput()))

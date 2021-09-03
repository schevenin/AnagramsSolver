import enchant

english_dictionary = enchant.Dict("en_US")

# lists
five_letter_combinations = []
four_letter_combinations = []
three_letter_combinations = []
two_letter_combinations = []
one_letter_combinations = []
combinations = []
uniques = []
words = []
one = []
two = []
three = []
four = []
five = []
six = []
counter = 0

# functions
def toString(List):
    return ''.join(List)


def cutLetter(string, length):
    combinations = []
    for letter in range(length):
        combinations.append(string[0:letter:] + string[letter+1::])
    return combinations


def permute(a, l, r):
    if l == r:
        global counter
        counter += 1
        word = toString(a)
        verifyWord(word)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


def findPermutations(letters):
    n = len(letters)
    a = list(letters)
    permute(a, 0, n - 1)


def verifyWord(word):
    if (english_dictionary.check(word)):
        if len(word) > 2:
            if word not in words:
                words.append(word)

def output(list):
    if (len(list) != 0):
        print(str(len(list[0])) + " letter words: ")
        print(', '.join(list))


# output
print("Anagrams Solver App")
letters = input("Type your six letters without spaces or special characters: ")

# append all possible outcomes to list
combinations.append(letters)

# create all length combinations of letters
five_letter_combinations = cutLetter(letters, 6)
for a in five_letter_combinations:
    combinations.append(a)
    for each in cutLetter(a, 5):
        four_letter_combinations.append(each)
for b in four_letter_combinations:
    combinations.append(b)
    for each in cutLetter(b, 4):
        three_letter_combinations.append(each)
for c in three_letter_combinations:
    combinations.append(c)
    for each in cutLetter(c, 3):
        two_letter_combinations.append(each)
for d in two_letter_combinations:
    combinations.append(d)
    for each in cutLetter(d, 2):
        one_letter_combinations.append(each)

# find permutations for all unique combinations
for combination in combinations:
    if combination not in uniques:
        uniques.append(combination)
        findPermutations(combination)

# group by length for output
for word in words:
    if (len(word) == 1):
        one.append(word)
    elif (len(word) == 2):
        two.append(word)
    elif (len(word) == 3):
        three.append(word)
    elif (len(word) == 4):
        four.append(word)
    elif (len(word) == 5):
        five.append(word)
    elif (len(word) == 6):
        six.append(word)

# output
print("")
print("Success!")
print(f'Found {len(words)} unique dictionary words from {counter} unique combinations: ')
print("")
output(six)
output(five)
output(four)
output(three)
output(two)
output(one)
print("")
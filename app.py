import enchant
import itertools

english_dictionary = enchant.Dict("en_US")

#lists
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


def permute(a, l, r):
    if l == r:
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

'''
# append all possible outcomes to list
combinations.append(letters)
print(combinations)
for i in range(6):
    five_listed_letters = list(letters)
    five_listed_letters.pop(i), five_listed_letters
    combinations.append(five_listed_letters)
    print(combinations)
    for x in range(5):
        four_listed_letters = list.copy(five_listed_letters)
        four_listed_letters.pop(x), four_listed_letters
        combinations.append(four_listed_letters)
        for y in range(4):
            three_listed_letters = list.copy(four_listed_letters)
            three_listed_letters.pop(y), three_listed_letters
            combinations.append(three_listed_letters)
            for z in range(3):
                two_listed_letters = list.copy(three_listed_letters)
                two_listed_letters.pop(z), two_listed_letters
                combinations.append(two_listed_letters)


# sort out duplicates
for i in combinations:
    if i not in uniques:
        counter += 1
        uniques.append(i)

# find permutations
for i in uniques:
    findPermutations(toString(i))
'''

combinations = list(itertools.permutations(letters))
for i in combinations:
    counter += 1
    if verifyWord(toString(i)):
        words.append(i)

# sort words into groups by length
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
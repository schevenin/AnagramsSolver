import enchant
from itertools import chain, combinations


def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        checkifword(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


def findPermutations(letters):
    n = len(letters)
    a = list(letters)
    permute(a, 0, n - 1)


def checkifword(word):
    if (english_dictionary.check(word)):
        if len(word) > 2:
            print(word)


english_dictionary = enchant.Dict("en_US")
print("Find Words Program v1.0")
letters = str(input("What letters are you given? "))

allCombinations = []
allCombinations.append(letters)

for i in range(6):
    five_listed_letters = list(letters)
    five_listed_letters.pop(i), five_listed_letters
    allCombinations.append(five_listed_letters)
    for x in range(5):
        four_listed_letters = list.copy(five_listed_letters)
        four_listed_letters.pop(x), four_listed_letters
        allCombinations.append(four_listed_letters)
        for y in range(4):
            three_listed_letters = list.copy(four_listed_letters)
            three_listed_letters.pop(y), three_listed_letters
            allCombinations.append(three_listed_letters)
            for z in range(3):
                two_listed_letters = list.copy(three_listed_letters)
                two_listed_letters.pop(z), two_listed_letters
                allCombinations.append(two_listed_letters)

uniqueList = []
for i in allCombinations:
    if i not in uniqueList:
        uniqueList.append(i)

for i in uniqueList:
    findPermutations(toString(i))
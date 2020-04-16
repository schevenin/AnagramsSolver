import enchant

#lists
allCombinations = []
uniqueList = []
listofwords = []
counter = 0

#functions
def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        word = toString(a)
        checkifword(word)
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
    global counter
    counter += 1
    if (english_dictionary.check(word)):
        if len(word) > 2:
            listofwords.append(word)



english_dictionary = enchant.Dict("en_US")
print("Find Words Program v1.0")
letters = input("What 6 letters are you given? ")

#append all possible outcomes to list
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


#sort out duplicates in list
for i in allCombinations:
    if i not in uniqueList:
        uniqueList.append(i)


#find permutations
for i in uniqueList:
    findPermutations(toString(i))


#order the permutations
print("")
listofwords = sorted(listofwords, key=len, reverse=True)
print(f'Found {len(listofwords)}/{counter}: ')
for i in listofwords:
    print(i)
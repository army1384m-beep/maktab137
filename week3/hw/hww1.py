from itertools import combinations
import copy
text = str(input("Please enter your sentence or words: "))
words = text.split()
print("Words :", words)

def comb_generator(words, sizes):
    for size in sizes:
        comb = combinations(words, size)
        for combo in comb:
            yield list(combo)

gen = comb_generator(words, [2, 3, 4])
two_comb = []
three_comb = []
four_comb = []

for combo in gen:
    if len(combo) == 2:
        two_comb.append(combo)
    elif len(combo) == 3:
        three_comb.append(combo)
    elif len(combo) == 4:
        four_comb.append(combo)


print("\nCombinations of 2 words:")
for combo in two_comb:
    print(combo)

print("\nCombinations of 3 words:")
for combo in three_comb:
    print(combo)

print("\nCombinations of 4 words:")
for combo in four_comb:
    print(combo)

two_shallow = copy.copy(two_comb)
two_deep = copy.deepcopy(two_comb)

three_shallow = copy.copy(three_comb) 
three_deep = copy.deepcopy(three_comb)

four_shallow = copy.copy(four_comb)
four_deep = copy.deepcopy(four_comb)

if two_comb:
    two_comb[0][0] = "137maktab"

print("\nAfter changing first word of first 2-word combination:")
print("Original two_comb:", two_comb)
print("Shallow copy:", two_shallow)
print("Deep copy:", two_deep)
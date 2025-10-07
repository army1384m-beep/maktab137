print("please enter your string1: ")
string1 = input()
print("pleast enter your string2: ")
string2 = input()

difference = 0
for letter in range(len(string1)):
    if string1[letter] != string2[letter]:
        difference += 1

print(f"The number of our contradictions is : {difference}")
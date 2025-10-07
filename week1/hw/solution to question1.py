# قسمت الف
print("enter your string: ")
text = str(input())
text = ("".join(text.split()))

# قسمت ب
x = ['a', 'o', 'u', 'e', 'i']
for vowel in x:
   text = text.replace(vowel, ".")

# قسمت ج
# result = text.swapcase()
final_result = (text[:: -1])
print(final_result)
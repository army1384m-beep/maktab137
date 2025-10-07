print("Please enter your name : ")
first_name = str(input())
print("Please enter the score : ")
score = int(input())

if score >= 90 :
    print(f"{first_name} : excellent score")

elif score >= 70 and score <= 90 :
    print(f"{first_name} : good score")

else:
    print(f"{first_name} : needs improvement")
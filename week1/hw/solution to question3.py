print("Enter your desired weather temperature: ")
temperature = int(input())

if temperature < 10:
    print("The weather is cold")

elif temperature <= 25:
    print("The weather is mild")
    
else:
    print("The weather is hot")
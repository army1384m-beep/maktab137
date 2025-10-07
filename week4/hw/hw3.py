our_list = [1, 2, 3, 1, 4, 2, 1]

def new_list(one_list):
    Repeating_element = {}
    for items in one_list:
        if items in Repeating_element:
             Repeating_element[items] += 1   
        else:
            Repeating_element[items] = 1   
    
    max_key = max(Repeating_element, key=Repeating_element.get)  
    return max_key

result = new_list(our_list)
print(f"Repetitive element: {result}")


# ls_list = ["ali", "sara", "mahdi", "sara", "mahdi", "sara"]

# def new_lst(just_list):
#     Repeating_elements = {}
#     for item in ls_list:
#         if item in Repeating_elements:
#          Repeating_elements[item] += 1

#     else:
#         Repeating_elements[item] = 1

#     max_repetition = max(Repeating_elements, key = Repeating_elements.get)
#     return max_repetition
# result = new_lst(ls_list)
# print(f"Most repeated element: {result}")
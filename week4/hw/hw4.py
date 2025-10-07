example = [1, [2, [3, 4]], 5]
def sum_nested(lst):
    if len(lst) == 0:  
        return 0
    
    first = lst[0]     
    other_members = lst[1:]      
    
    if type(first) == list: 
        return sum_nested(first) + sum_nested(other_members)
    else:  
        return first + sum_nested(other_members)
    
print(sum_nested(example))
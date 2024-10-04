# 1. "Triple" function
def triple(x):
    """multiplies input by three"""
    result = 3 * x
    return result

# 2. "Subtract" function
def subtract(a, b):
    """subtract the second number from the first"""
    result = a - b
    return result

# 3. "Dictionary_maker" function, returning a dictionary from a list of tuples.
def dictionary_maker(my_list):
    """returns a dictionary where the keys are the first element from each tuple in the list, 
    and the values are the second element"""
    my_dict = {}
    for x in my_list:
        my_dict[x[0]] = x[1]

    return(my_dict)
def find_extremes(lst):
    """
    function takes list of numbers and returns the highest and lowest value in the list.
    If the list does not have at least 2 unique numbers, it returns the string: “error: list does not meet specifications”.
    """
    if len(set(lst)) < 2:
        return "error: list does not meet specifications"
    else:
        return min(lst), max(lst)
    
my_list = [3, 5, 1, 8, 2, 9]
result = find_extremes(my_list)
print(result)  

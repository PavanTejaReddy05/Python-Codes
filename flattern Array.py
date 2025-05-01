def Pl(lst):
    lst1 = []  # Initialize an empty list to store flattened elements
    for i in lst:
        if isinstance(i, list):  # If the element is a list, recurse into it
            lst1.extend(Pl(i))  # Flatten the sublist and extend lst1 with the result
        else:
            lst1.append(i)  # Otherwise, append the element to lst1
        return lst1
# Example usage
lst = [1, 2, 3, [4, [11, 12], 5], 6, 7, [8, 9, [13,14,15,[[1,2,3]]]], 10]
print(Pl(lst))  # Output: [1, 2, 3, 4, 11, 12, 5, 6, 7, 8, 9, 10]
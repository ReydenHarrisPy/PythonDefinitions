def highest_even(list):
    even = [] #make new list of evens
    for item in list: # for loop to append all even values to new list
        if item % 2 == 0:
            even.append(item)
    return max(even) #return the highest value from new list of even.


print(highest_even([10,2,56,11,89]))
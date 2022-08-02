# *args **kwargs

# args
def super_func(*args): # this allows function to accept any number of arguements
    print(args) # this is a tuple without *
    return sum(args)

#print(super_func(1,2,3,4,5))


#kwargs

def super_function(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_function(1,2,3,4,5, num1=5, num2=10))

#rule: parms, *args, default params, **kwargs
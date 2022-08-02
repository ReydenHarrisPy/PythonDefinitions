# return

#def sum(num1, num2):
  #return num1 + num2

#print(sum(10,5))

#functions can retrun something or modify something

# Nested function, i can redefine a function. 
def sum(num1, num2):
  def another_sum(n1, n2):
    return n1 - n2
  return another_sum(num1, num2)


tot = sum(10, 80)

print(tot)


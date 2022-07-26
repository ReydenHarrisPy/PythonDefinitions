amazon_cart = ['notebooks',
               'paper',
              'pencils',
              'usb stick',
               
              ]
amazon_cart[0] = 'laptop' # assign 'laptop to 0 in list'

new_cart = amazon_cart[:]#copy entire list with out having to change values of list

new_cart[0] = 'pasta'



print(new_cart)

print(amazon_cart)
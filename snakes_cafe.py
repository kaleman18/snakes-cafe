import sys

print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************""")


status = True
ordernumber = 1

while status == True:
    order2 = input('> ')
    if order2 == "quit":
        status= False
        sys.exit()
        
    if ordernumber == 1:
        print(f'**{ordernumber} order of {order2} has been added to your meal **')
    elif ordernumber > 1:
        print(f'**{ordernumber} orders of {order2} have been added to your meal**')
    
    ordernumber +=1




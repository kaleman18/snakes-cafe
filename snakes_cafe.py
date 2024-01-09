
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
order = input('> ')
ordernumber = 1

while order != 'quit':
    order = input('> ')
    if ordernumber == 1:
        print(f'**{ordernumber} order of {order} has been added to your meal **')
    elif ordernumber > 1:
        print(f'**{ordernumber} orders of {order} have been added to your meal**')
    ordernumber +=1




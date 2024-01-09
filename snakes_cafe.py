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
orderItem = []


while status == True:
    order2 = input('> ')
    orderItem.append(order2)
    if order2 == "quit":
        status= False
        sys.exit()

    if orderItem.count(order2) == 1:
        print(f'**{orderItem.count(order2)} order of {order2} has been added to your meal **')
    elif orderItem.count(order2) > 1:
        print(f'**{orderItem.count(order2)} orders of {order2} have been added to your meal**')




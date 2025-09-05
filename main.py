from pyscript import display
from datetime import datetime, timedelta, date, time

restaurant_name = 'Mr Choy' #String
owner_name = 'Stephen Choy' #String
year_established = 2017 #Integer
popular_item = 'Mixed Vegetable Fried Rice' #String
has_delivery = True #Boolean
product_names = ['Mushroom Fried Rice', 'Mixed Vegetable Fried Rice', 'Chicken Fried Rice', 'Roast Duck with Plum Sauce', 'Ribs in Hoi Sin Sauce'] #List
menu_prices = [7.50, 8.00, 8.00, 9.30, 8.65] #List
business_hours = {"from": time(hour=7, minute=30), "to": time(hour=17, minute=30)} #Dictionary
common_allergens = ('peanut', 'shellfish', 'egg') #Tuple
tax_rate = 0.072 #Integer

#Header

display(restaurant_name, target='header')
display(owner_name, target='header')
display(f'since {year_established}', target='header')

# Menu

display(product_names[0], target='f1')
display(product_names[1], target='f2')
display(product_names[2], target='f3')
display(product_names[3], target='f4')
display(product_names[4], target='f5')

display(f'${menu_prices[0]}', target='p1')
display(f'${menu_prices[1]}', target='p2')
display(f'${menu_prices[2]}', target='p3')
display(f'${menu_prices[3]}', target='p4')
display(f'${menu_prices[4]}', target='p5')
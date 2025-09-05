from pyscript import display
from datetime import datetime, timedelta, date, time
import pandas as pd

restaurant_name = 'Mr Choy'
owner_name = 'Stephen Choy'
year_established = 2017
popular_item = 'Mixed Vegetable Fried Rice'
has_delivery = True
product_names = ['Mushroom Fried Rice', 'Mixed Vegetable Fried Rice', 'Chicken Fried Rice', 'Roast Duck with Plum Sauce', 'Ribs in Hoi Sin Sauce']
menu_prices = [7.50, 8.00, 8.00, 9.30, 8.65]
business_hours = {"from": time(hour=7, minute=30), "to": time(hour=17, minute=30)}
common_allergens = {'peanut', 'shellfish', 'egg'}
tax_rate = 0.072

display(restaurant_name, target='header')
display(owner_name, target='header')
display(year_established, target='header')

df = pd.DataFrame({
    "Product Name": product_names, 
    "Price": menu_prices
})

df.index += 1

display(df, target="pandas-output-inner", append="False")
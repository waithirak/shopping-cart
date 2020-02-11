# shopping_cart.py
import datetime
#date idea source: https://docs.python.org/3/library/datetime.html 
#from pprint import pprint
#USD FORMAT SOURCE: MY POOR ROOMMATE CHRISTINE WHO JUST WANTS ME TO TURN OFF THE LIGHTS SO SHE CAN SLEEP


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)


# TODO: write some Python code here to produce the desired output


#Info Capture: inputs 

total_price = 0
selected_ids = []


while True:
    selected_id = input("Please input a product identifier:  ")
    if selected_id == "DONE": 
        break
    elif int(selected_id)> 20:
        print("ARE YOU SURE THIS IS A VALID PRODUCT IDENTIFIER? PLEASE TRY AGAIN")
        next
    else:
        selected_ids.append(selected_id)



print("-------------------------------")
print("FINE FOODS GROCERY")
print("FIND US AT: WWW.FINE-FOODS.COM")
print("OR CALL US AT: (202) 452 2290")
print("-------------------------------")
print("CHECKEDOUT AT: ")
now = datetime.datetime.now()
print(now.strftime("%m/%d/%Y  %H:%M"))          #SEE TOP IMPORT FOR SOURCE
print("-------------------------------")

for selected_id in selected_ids: 
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product ["price"]
        print("SELECTED PRODUCTS: " + matching_product["name"] +  " " + '${:,.2f}'.format(matching_product["price"] ))

sales_tax = float(total_price * 0.0875)
#generally tax = rate * total sales 
#so maybe just concatonate??
sum = float(total_price * 0.0875) + float(total_price)


#Info Display: outputs

print("SUBTOTAL: " + '${:,.2f}'.format(total_price))    #USD SOURCE AT THE TOP
print("SALES TAX: " + '${:,.2f}'.format(sales_tax))
print ("TOTAL: " + '${:,.2f}'.format(sum))
print("--------------------------------")
print("THANK YOU FOR SHOPPING AT FINE FOODS")
print("                                      ")
# i just need space between the end of this code and the next command so thats why theres an empty print()



#REQUIREMENTS:
#ALL REQUIREMENTS DONE
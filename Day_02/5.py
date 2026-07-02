"""Create a list of 5 Product prices.
Ask the user to enter:
A product index
A coupon code
Rules:
if the index is invalid print invalid product
otherwise,get the selected product's price
if the coupon code is SAVE10,give a 10 percent discount.
if it is SAVE20 and the price is greater than 1000 ruppes give a 20 percent discount.
otherwise,give no discount.
print the final price whether the discount was applied"""




Product_price = [89,300,200,988,456]
Product_index = int(input("Enter the product index(0-4)"))
if (0<=Product_index<=4):
    coupon_code=input("Enter the coupon code")
    if (coupon_code=="SAVE10"):
        discount=(0.1*Product_price[Product_index])
        price = Product_price[Product_index-discount]
        print(f"Final price is with 10 percent Discount {price}")
    elif((coupon_code=="SAVE20")and(Product_price[Product_index]>1000)):
        discount = (0.2*Product_price[Product_index])
        price = Product_price[Product_index]-discount
        print(f"Final price is with 20 percent Discount {price}")
    else:
        print("No Discount")
        price = (Product_price[Product_index])
        print(f"Final price is {price}")
else:
    print("Invalid Product index")



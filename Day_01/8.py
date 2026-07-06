"""a shop sell 3 identical iteam:
input-price,gst%,discount%
calculate-total price,gst amount,price after adding gst,discount amount,final payable amount"""


price1 = int(input("enter the price of iteam:"))
gst = int(input("enter the gst percentage:"))
discount = int(input("enter the discount percentage:"))

total_price = (price1*3)
gst_amount = ((gst/100)*total_price)
price_with_gst = (total_price + gst_amount)
discount_amount = ((discount/100)*price_with_gst)
final_amount = (price_with_gst - discount_amount)

final_amount1 = round(final_amount,2)
total_price1 = round(total_price,2)
gst_amount1 = round(gst_amount,2)
price_with_gst1 = round(price_with_gst,2)
discount_amount1 = round(discount_amount,2)


print(f"totalprice: {total_price1}\nGST amount: {gst_amount1}\nprice after adding GST: {price_with_gst1}\nDiscount amount {discount_amount1}\nFinal payable amount: {final_amount1}")
"""A person deposits ₹P in a bank.

Every year:

Money increases by 8%.
Inflation decreases purchasing power by 5%.

Find:

Actual money after 5 years.
Real value of money after considering inflation.

This question tests whether you understand that growth and decrease happen one after another, not simply 8%-5%=3%."""


money = int(input("enter your salary:"))

actual_money = (money*(1.08**5))
inflation_money = (actual_money*(.95**5))


print(f"actual salary after 5 year:{actual_money}\nactual money after considerinf inflation:{inflation_money}")
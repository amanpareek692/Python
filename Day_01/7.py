"""take:
total seconds:
convert into:
hours,minutes and remaining seconds"""




seconds = int(input("enter the total seconds:"))


minutes = seconds//60
hours = minutes//60
minutes1 = minutes%60
seconds1 = seconds%60


print("hour:",hours)
print("minutes:",minutes1)
print("seconds:",seconds1)
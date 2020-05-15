# INPUTS

items_total = int(input("Enter the amount of items you are paying for: "))

first_item = 10.95
remaining_item = (items_total - 1 ) * 2.95

if items_total == 1 :
    print("You have purchased 1 item and the shipping fee for this item is $" , first_item , ".")
elif items_total > 1 :
    print("You have purchased" , items_total , "items and the shipping fee for them is $" , first_item + remaining_item , ".")
else :
    print("The number of items you inputed is incorrect.")
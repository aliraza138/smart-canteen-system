# 1 condition - if statement
# 1 condition, 2 outputs - if-else statement
# 2 conditions, 3 outputs - if-elif-else statement

# Topic 1: Conditional Statements 
# Program 1: Smart Canteen Discount System
# Topic: if, elif, else, comparison operators, and logical thinking.
# Real-World Scenario
# Imagine a college canteen where students receive discounts based 
# on their total bill.

# The canteen follows these rules:
# - If the bill is Rs. 3,000 or more, the student receives a 
# 20% discount.
# - If the bill is Rs. 2,000 or more but less than Rs. 3,000, 
# the student receives a 10% discount.
# - If the bill is Rs. 1,000 or more but less than Rs. 2,000, 
# the student receives a 5% discount.
# - If the bill is less than Rs. 1,000, no discount is provided.
# - The program must display the original bill, discount amount,
# and final payable amount.

print("===== SMART CANTEEN =====")
bill_amount = float(input("Enter your total bill amount (Rs.): "))
if bill_amount <= 0:
    print("Invalid Bill Amount!")
else:
     if bill_amount >= 3000:
         discount_rate = 20
     elif bill_amount >= 2000:
         discount_rate = 10
     elif bill_amount >= 1000:
          discount_rate = 5
     else:
         discount_rate = 0
discount_amount = bill_amount * discount_rate / 100
final_amount = bill_amount - discount_amount

print("\n===== BILL SUMMARY =====")
print(f"Original Bill: Rs. {bill_amount:.2f}")
print(f"Discount Rate: {discount_rate}%")
print(f"Discount Amount: Rs. {discount_amount:.2f}")
print(f"Final Payable: Rs. {final_amount:.2f}")


# -----------------------------------------------------------
# IMPROVEMENT 1: Special Bonus Discount for 4000+ shopping!
# -----------------------------------------------------------
bonus_discount = 0
if bill_amount >= 4000:
    bonus_discount = 100
    print("\n🎉 Congratulations! Shopping above Rs. 4000 qualifies for an EXTRA Rs. 100 Gift Discount!")

# Total Discount calculation
total_discount = discount_amount + bonus_discount
final_bill = bill_amount - total_discount

# Bill Summary Print karna
print("\n------------- BILL RECEIPT -------------")
print(f"Original Bill      : Rs. {bill_amount:.2f}")
print(f"Standard Discount  : {discount_amount}% (Rs. {discount_amount:.2f})")
if bonus_discount > 0:
    print(f"Bonus Gift Discount: Rs. {bonus_discount:.2f}")
print(f"Total Discount     : Rs. {total_discount:.2f}")
print("----------------------------------------")
print(f"FINAL PAYABLE BILL : Rs. {final_amount:.2f}")
print("----------------------------------------")


# -----------------------------------------------------------
# IMPROVEMENT 2: Active Membership Discount for bills under 1000
# -----------------------------------------------------------
if bill_amount < 1000:
    member_ship = int(input("Do You Have Active Membership (1 for Yes, 0 for No): "))
    if member_ship == 1:
        discount_rate = 2
        print("\n🎉 Congratulations! Active Membership qualifies you for a 2% Discount!")
    else:
        discount_rate = 0

# Discount amount calculation
discount_amount = (bill_amount * discount_rate) / 100

# Total Discount calculation (agar bonus discount bhi sath hai)
total_discount = discount_amount + bonus_discount
final_amount = bill_amount - total_discount

# Bill Summary Print karna
print("\n------------- BILL RECEIPT -------------")
print(f"Original Bill      : Rs. {bill_amount:.2f}")
print(f"Discount Rate      : {discount_rate}%")
print(f"Discount Amount    : Rs. {discount_amount:.2f}")
if bonus_discount > 0:
    print(f"Bonus Gift Discount: Rs. {bonus_discount:.2f}")
print(f"Total Discount     : Rs. {total_discount:.2f}")
print("----------------------------------------")
print(f"FINAL PAYABLE BILL : Rs. {final_amount:.2f}")
print("----------------------------------------")
# Practice Question:
# Student Challenge
# Ask students to extend the program with these features:
# 1. If the bill is less than or equal to zero, display an invalid 
# bill message.
# 2. If the student has a membership card, provide an additional 5% 
# discount.
# 3. Display a message saying "Congratulations! You saved Rs. X" 
# when a discount is applied.
# Teaching question: Why do we use elif instead of writing several 
# independent if statements?



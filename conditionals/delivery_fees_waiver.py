order_amount= int(input("Enter order amount: "))

devlivery_fees= 0


# ternary operator

devlivery_fees="0" if order_amount>300 else 50

print(f"Delivery fees: {devlivery_fees}")
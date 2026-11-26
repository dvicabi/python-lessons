customer_ids = [101, 102]
customer_active = [True, False]
customer_zones = [1, 2]
customer = 101
cart = [[0, 2], [0, 1], [1, 2]]
stock = [5, 4, 7]
prices = [10, 8, 5]
paid = 50
delivery_zones = [2, 1, 1]
delivery_free = [2, 0, 3]

# TEAM_CODE
# 01 customers
customer_ok = False
zone = -1
fee = 0
for i in range(len(customer_ids)):
    if customer_ids[i] == customer and customer_active[i]:
        if customer_zones[i] == 1 or customer_zones[i] == 2:
            customer_ok = True
            zone = customer_zones[i]
if customer_ok:
    fee = 4
    if zone == 2:
        fee = 6

# 02 cart
needed = []
for value in stock:
    needed.append(0)
cart_ok = customer_ok and len(cart) > 0
if customer_ok:
    for row in cart:
        item = row[0]
        qty = row[1]
        if item < 0 or item >= len(needed) or qty <= 0:
            cart_ok = False
        else:
            needed[item] += qty

# 03 inventory
proposed_stock = []
for qty in stock:
    proposed_stock.append(qty)
stock_ok = cart_ok
for i in range(len(stock)):
    if needed[i] > stock[i]:
        stock_ok = False
if stock_ok:
    for i in range(len(stock)):
        proposed_stock[i] -= needed[i]

# 04 pricing
total = -1
discount = 0
if stock_ok:
    gross = 0
    for i in range(len(needed)):
        gross += needed[i] * prices[i]
        if needed[i] >= 3:
            discount += needed[i] * 2
    total = gross - discount + fee

# 05 payments
payment_ok = stock_ok and total >= 0 and paid >= total
change_proposed = 0
if payment_ok:
    change_proposed = paid - total

# 06 fulfillment
slot = -1
if payment_ok:
    for i in range(len(delivery_zones)):
        if slot == -1 and delivery_zones[i] == zone and delivery_free[i] > 0:
            slot = i
stock_after = []
delivery_after = []
for qty in stock:
    stock_after.append(qty)
for value in delivery_free:
    delivery_after.append(value)
revenue = 0
refund = paid
if not customer_ok:
    result = "CUSTOMER"
elif not cart_ok:
    result = "CART"
elif not stock_ok:
    result = "STOCK"
elif not payment_ok:
    result = "PAYMENT"
elif slot == -1:
    result = "DELIVERY"
else:
    result = "OK"
    for i in range(len(stock_after)):
        stock_after[i] = proposed_stock[i]
    delivery_after[slot] -= 1
    revenue = total
    refund = change_proposed

# FINAL_REPORT
print("result:", result)
print("total:", total)
print("discount:", discount)
print("slot:", slot)
print("stock_after:", stock_after)
print("delivery_after:", delivery_after)
print("revenue:", revenue)
print("refund:", refund)

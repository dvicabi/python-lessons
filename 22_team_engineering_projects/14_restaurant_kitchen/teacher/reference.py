order_id = 51
used = [50]
mode = 1
cart = [[0, 1], [1, 2], [0, 1]]
special = [True, True, False]
recipes = [[2, 1, 0], [0, 1, 2], [1, 0, 1]]
stock = [8, 5, 8]
stations = [0, 1, 0]
minutes = [3, 2, 4]
station_free = [8, 6]
prices = [12, 8, 15]
paid = 40

# TEAM_CODE
# 01 requests
request_ok = order_id > 0 and order_id not in used and (mode == 0 or mode == 1) and len(cart) > 0

# 02 menu
quantities = []
for value in special:
    quantities.append(0)
menu_ok = request_ok
if request_ok:
    for line in cart:
        item = line[0]
        qty = line[1]
        if item < 0 or item >= len(special) or qty <= 0:
            menu_ok = False
        elif mode == 1 and not special[item]:
            menu_ok = False
        else:
            quantities[item] += qty

# 03 ingredients
needed = []
for value in stock:
    needed.append(0)
ingredients_ok = menu_ok
if menu_ok:
    for i in range(len(quantities)):
        for j in range(len(stock)):
            needed[j] += quantities[i] * recipes[i][j]
    for j in range(len(stock)):
        if needed[j] > stock[j]:
            ingredients_ok = False

# 04 kitchen
load = []
for value in station_free:
    load.append(0)
kitchen_ok = ingredients_ok
if ingredients_ok:
    for i in range(len(quantities)):
        load[stations[i]] += quantities[i] * minutes[i]
    for i in range(len(load)):
        if load[i] > station_free[i]:
            kitchen_ok = False

# 05 billing
total = -1
change_due = 0
payment_ok = False
if kitchen_ok:
    total = 0
    count = 0
    for i in range(len(quantities)):
        total += quantities[i] * prices[i]
        count += quantities[i]
    if count >= 4:
        total -= 4
    if paid >= total and paid >= 0:
        payment_ok = True
        change_due = paid - total

# 06 commit
stock_after = []
station_after = []
used_after = []
for value in stock:
    stock_after.append(value)
for value in station_free:
    station_after.append(value)
for value in used:
    used_after.append(value)
revenue = 0
refund = paid
if not request_ok:
    result = "REQUEST"
elif not menu_ok:
    result = "MENU"
elif not ingredients_ok:
    result = "INGREDIENTS"
elif not kitchen_ok:
    result = "KITCHEN"
elif not payment_ok:
    result = "PAYMENT"
else:
    result = "OK"
    for i in range(len(needed)):
        stock_after[i] -= needed[i]
    for i in range(len(load)):
        station_after[i] -= load[i]
    used_after.append(order_id)
    revenue = total
    refund = change_due

# FINAL_REPORT
print("result:", result)
print("total:", total)
print("stock_after:", stock_after)
print("station_after:", station_after)
print("used_after:", used_after)
print("revenue:", revenue)
print("refund:", refund)

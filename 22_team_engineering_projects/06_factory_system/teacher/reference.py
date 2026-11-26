product_ids = [10, 20]
recipes = [[2, 1, 0], [1, 2, 1]]
product = 20
quantity = 3
materials = [8, 15, 10]
machine_capacity = [2, 8, 6]
machine_rate = [2, 3, 2]
machine_minutes = [12, 20, 8]
quality_scores = [80, 75, 90]
shipping_free = [2, 5, 3]

# TEAM_CODE
# 01 orders
product_index = -1
for i in range(len(product_ids)):
    if product_ids[i] == product:
        product_index = i
order_ok = product_index != -1 and quantity > 0
if not order_ok:
    product_index = -1

# 02 materials
needed = []
for amount in materials:
    needed.append(0)
materials_ok = order_ok
if order_ok:
    for i in range(len(materials)):
        needed[i] = recipes[product_index][i] * quantity
        if needed[i] > materials[i]:
            materials_ok = False

# 03 machines
machine = -1
minutes = 0
if materials_ok:
    for i in range(len(machine_rate)):
        time = machine_rate[i] * quantity
        if machine_capacity[i] >= quantity and time <= machine_minutes[i]:
            if machine == -1 or time < minutes:
                machine = i
                minutes = time

# 04 quality
quality_ok = machine != -1 and len(quality_scores) == quantity
bad_count = 0
if machine != -1:
    for value in quality_scores:
        if value < 70 or value > 100:
            quality_ok = False
            bad_count += 1

# 05 shipping
shipping = -1
if quality_ok:
    for i in range(len(shipping_free)):
        if shipping_free[i] >= quantity:
            if shipping == -1 or shipping_free[i] < shipping_free[shipping]:
                shipping = i

# 06 controller
materials_after = []
minutes_after = []
shipping_after = []
for value in materials:
    materials_after.append(value)
for value in machine_minutes:
    minutes_after.append(value)
for value in shipping_free:
    shipping_after.append(value)
fulfilled = 0
if not order_ok:
    result = "ORDER"
elif not materials_ok:
    result = "MATERIALS"
elif machine == -1:
    result = "MACHINE"
elif not quality_ok:
    result = "QUALITY"
elif shipping == -1:
    result = "SHIPPING"
else:
    result = "OK"
    for i in range(len(needed)):
        materials_after[i] -= needed[i]
    minutes_after[machine] -= minutes
    shipping_after[shipping] -= quantity
    fulfilled = quantity

# FINAL_REPORT
print("result:", result)
print("machine:", machine)
print("minutes:", minutes)
print("bad_count:", bad_count)
print("shipping:", shipping)
print("materials_after:", materials_after)
print("minutes_after:", minutes_after)
print("shipping_after:", shipping_after)
print("fulfilled:", fulfilled)

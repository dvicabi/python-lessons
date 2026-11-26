product_ids = [10, 20, 30]
stock = [6, 5, 2]
weights = [2, 3, 4]
product = 20
quantity = 3
pack_limit = 10
vehicle_caps = [8, 12, 10]
vehicle_range = [15, 20, 9]
route_dist = [7, 9]
route_delay = [3, 0]
deadline = 10

# TEAM_CODE
# 01 orders
product_index = -1
for i in range(len(product_ids)):
    if product_ids[i] == product:
        product_index = i
order_ok = product_index != -1 and quantity > 0
if not order_ok:
    product_index = -1

# 02 inventory
stock_ok = False
remaining_stock = -1
if order_ok and stock[product_index] >= quantity:
    stock_ok = True
    remaining_stock = stock[product_index] - quantity

# 03 packing
load = 0
pack_ok = False
if stock_ok:
    load = quantity * weights[product_index]
    pack_ok = load <= pack_limit

# 04 vehicles
candidates = []
if pack_ok:
    for i in range(len(vehicle_caps)):
        if vehicle_caps[i] >= load:
            candidates.append(i)

# 05 routing
vehicle = -1
route = -1
eta = -1
travel_cost = 0
for v in candidates:
    for r in range(len(route_dist)):
        time = route_dist[r] + route_delay[r]
        cost = route_dist[r] * 2
        if cost <= vehicle_range[v] and time <= deadline:
            if vehicle == -1 or time < eta or (time == eta and vehicle_caps[v] < vehicle_caps[vehicle]):
                vehicle = v
                route = r
                eta = time
                travel_cost = cost

# 06 dispatch
stock_after = []
range_after = []
for value in stock:
    stock_after.append(value)
for value in vehicle_range:
    range_after.append(value)
if not order_ok:
    result = "ORDER"
elif not stock_ok:
    result = "STOCK"
elif not pack_ok:
    result = "PACK"
elif len(candidates) == 0:
    result = "VEHICLE"
elif vehicle == -1:
    result = "ROUTE"
else:
    result = "OK"
    stock_after[product_index] = remaining_stock
    range_after[vehicle] -= travel_cost

# FINAL_REPORT
print("result:", result)
print("vehicle:", vehicle)
print("route:", route)
print("eta:", eta)
print("stock_after:", stock_after)
print("range_after:", range_after)

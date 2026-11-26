stations = [1, 2, 3, 4]
origin = 1
destination = 3
group_size = 2
earliest = 0
latest = 30
budget = 18
ticket = 31
used = [30]
from_station = [1, 2, 1, 1, 4]
to_station = [2, 3, 3, 4, 3]
departs = [0, 12, 5, 2, 13]
arrives = [10, 20, 25, 11, 19]
seats = [3, 3, 4, 2, 2]
fares = [3, 4, 8, 4, 5]
paid = 18

# TEAM_CODE
# 01 requests
request_ok = origin in stations and destination in stations and origin != destination and group_size > 0 and earliest <= latest and budget >= 0 and ticket > 0 and ticket not in used

# 02 routes
routes = []
if request_ok:
    for i in range(len(from_station)):
        if from_station[i] == origin and departs[i] >= earliest:
            if to_station[i] == destination and arrives[i] <= latest:
                routes.append([i])
            elif to_station[i] != destination:
                for j in range(len(from_station)):
                    if j != i and from_station[j] == to_station[i] and to_station[j] == destination and departs[j] >= arrives[i] + 2 and arrives[j] <= latest:
                        routes.append([i, j])

# 03 capacity
seat_routes = []
for path in routes:
    ok = True
    for leg in path:
        if seats[leg] < group_size:
            ok = False
    if ok:
        seat_routes.append(path)

# 04 pricing
chosen = []
eta = -1
total = -1
for path in seat_routes:
    price = 0
    for leg in path:
        price += fares[leg] * group_size
    arrival = arrives[path[len(path) - 1]]
    if price <= budget:
        if len(chosen) == 0 or arrival < eta or (arrival == eta and price < total):
            chosen = path
            eta = arrival
            total = price

# 05 payments
payment_ok = len(chosen) > 0 and paid >= total and paid >= 0
change_due = 0
if payment_ok:
    change_due = paid - total

# 06 ticketing
seats_after = []
used_after = []
for value in seats:
    seats_after.append(value)
for value in used:
    used_after.append(value)
revenue = 0
refund = paid
if not request_ok:
    result = "REQUEST"
elif len(routes) == 0:
    result = "ROUTE"
elif len(seat_routes) == 0:
    result = "SEATS"
elif len(chosen) == 0:
    result = "BUDGET"
elif not payment_ok:
    result = "PAYMENT"
else:
    result = "OK"
    for leg in chosen:
        seats_after[leg] -= group_size
    used_after.append(ticket)
    revenue = total
    refund = change_due

# FINAL_REPORT
print("result:", result)
print("chosen:", chosen)
print("eta:", eta)
print("total:", total)
print("seats_after:", seats_after)
print("used_after:", used_after)
print("revenue:", revenue)
print("refund:", refund)

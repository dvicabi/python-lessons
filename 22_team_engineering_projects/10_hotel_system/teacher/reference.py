guests = 3
start = 1
nights = 3
budget = 260
booking = 21
used = [20]
caps = [2, 4, 3]
rates = [60, 90, 80]
calendar = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 20]]
paid = 260

# TEAM_CODE
# 01 requests
request_ok = guests > 0 and start >= 0 and nights > 0 and budget >= 0 and booking > 0 and booking not in used
end_day = -1
if request_ok:
    end_day = start + nights

# 02 rooms
room_candidates = []
if request_ok:
    for i in range(len(caps)):
        if caps[i] >= guests:
            room_candidates.append(i)

# 03 availability
available_rooms = []
for i in room_candidates:
    ok = end_day <= len(calendar[i])
    if ok:
        for d in range(end_day - start):
            if calendar[i][start + d] != 0:
                ok = False
    if ok:
        available_rooms.append(i)

# 04 pricing
room = -1
total = -1
for i in available_rooms:
    price = rates[i] * nights
    if nights >= 3:
        price -= 10
    if price <= budget:
        if room == -1 or price < total or (price == total and caps[i] < caps[room]):
            room = i
            total = price

# 05 payments
payment_ok = room != -1 and paid >= total and paid >= 0
change_due = 0
if payment_ok:
    change_due = paid - total

# 06 booking
calendar_after = []
used_after = []
for line in calendar:
    row_copy = []
    for value in line:
        row_copy.append(value)
    calendar_after.append(row_copy)
for value in used:
    used_after.append(value)
revenue = 0
refund = paid
if not request_ok:
    result = "REQUEST"
elif len(room_candidates) == 0:
    result = "ROOM"
elif len(available_rooms) == 0:
    result = "DATES"
elif room == -1:
    result = "BUDGET"
elif not payment_ok:
    result = "PAYMENT"
else:
    result = "OK"
    for d in range(nights):
        calendar_after[room][start + d] = booking
    used_after.append(booking)
    revenue = total
    refund = change_due

# FINAL_REPORT
print("result:", result)
print("room:", room)
print("total:", total)
print("revenue:", revenue)
print("refund:", refund)
print("calendar_after:", calendar_after)
print("used_after:", used_after)

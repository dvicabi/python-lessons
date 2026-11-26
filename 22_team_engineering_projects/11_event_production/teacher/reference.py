event_id = 21
used = [20]
guests = 40
need = 5
budget = 180
caps = [30, 50, 60]
available = [True, True, True]
built_in = [3, 2, 4]
prices = [60, 90, 100]
setup_staff = [1, 1, 0]
equipment = 4
staff = 4

# TEAM_CODE
# 01 requests
request_ok = event_id > 0 and event_id not in used and guests > 0 and need >= 0 and budget >= 0

# 02 halls
hall_candidates = []
if request_ok:
    for i in range(len(caps)):
        if available[i] and caps[i] >= guests:
            hall_candidates.append(i)

# 03 equipment
extra_by_hall = []
equipment_candidates = []
for value in caps:
    extra_by_hall.append(-1)
for i in hall_candidates:
    extra = need - built_in[i]
    if extra < 0:
        extra = 0
    extra_by_hall[i] = extra
    if extra <= equipment:
        equipment_candidates.append(i)

# 04 staff
staff_by_hall = []
staff_candidates = []
for value in caps:
    staff_by_hall.append(-1)
rounded = guests + 19
for i in equipment_candidates:
    required = rounded // 20 + setup_staff[i]
    staff_by_hall[i] = required
    if required <= staff:
        staff_candidates.append(i)

# 05 pricing
hall = -1
total = -1
for i in staff_candidates:
    cost = prices[i] + extra_by_hall[i] * 8 + staff_by_hall[i] * 15
    if cost <= budget and (hall == -1 or cost < total):
        hall = i
        total = cost

# 06 commit
available_after = []
used_after = []
for flag in available:
    available_after.append(flag)
for value in used:
    used_after.append(value)
equipment_after = equipment
staff_after = staff
if not request_ok:
    result = "REQUEST"
elif len(hall_candidates) == 0:
    result = "HALL"
elif len(equipment_candidates) == 0:
    result = "EQUIPMENT"
elif len(staff_candidates) == 0:
    result = "STAFF"
elif hall == -1:
    result = "BUDGET"
else:
    result = "OK"
    available_after[hall] = False
    equipment_after -= extra_by_hall[hall]
    staff_after -= staff_by_hall[hall]
    used_after.append(event_id)

# FINAL_REPORT
print("result:", result)
print("hall:", hall)
print("total:", total)
print("available_after:", available_after)
print("equipment_after:", equipment_after)
print("staff_after:", staff_after)
print("used_after:", used_after)

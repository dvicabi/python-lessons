batch_id = 71
used = [70]
items = [[0, 3, 0], [1, 4, 0], [0, 2, 0], [2, 2, 0], [1, 1, 1]]
bad_limit = [1, 1, 1]
bin_type = [0, 1, 0, 2]
free = [3, 5, 4, 3]
rates = [2, 3, 1]
fund = 30

# TEAM_CODE
# 01 intake
request_ok = batch_id > 0 and batch_id not in used and len(items) > 0

# 02 sorting
good = [0, 0, 0]
bad = [0, 0, 0]
sort_ok = request_ok
if request_ok:
    for row in items:
        kind = row[0]
        weight = row[1]
        flag = row[2]
        if kind < 0 or kind > 2 or weight <= 0 or (flag != 0 and flag != 1):
            sort_ok = False
        elif flag == 0:
            good[kind] += weight
        else:
            bad[kind] += weight

# 03 quality
quality_ok = sort_ok
total_good = 0
for i in range(3):
    total_good += good[i]
    if bad[i] > bad_limit[i]:
        quality_ok = False
if total_good == 0:
    quality_ok = False
accepted = [0, 0, 0]
if quality_ok:
    for i in range(3):
        accepted[i] = good[i]

# 04 allocation
plan = []
for value in free:
    plan.append(0)
capacity_ok = quality_ok
if quality_ok:
    for kind in range(3):
        left = accepted[kind]
        for i in range(len(free)):
            if bin_type[i] == kind:
                take = left
                if take > free[i]:
                    take = free[i]
                plan[i] = take
                left -= take
        if left > 0:
            capacity_ok = False

# 05 credit
credit = 0
credit_ok = False
if capacity_ok:
    for i in range(3):
        credit += accepted[i] * rates[i]
    credit_ok = credit <= fund

# 06 commit
free_after = []
used_after = []
for value in free:
    free_after.append(value)
for value in used:
    used_after.append(value)
fund_after = fund
paid_credit = 0
if not request_ok:
    result = "REQUEST"
elif not sort_ok:
    result = "SORT"
elif not quality_ok:
    result = "QUALITY"
elif not capacity_ok:
    result = "CAPACITY"
elif not credit_ok:
    result = "CREDIT"
else:
    result = "OK"
    for i in range(len(free)):
        free_after[i] -= plan[i]
    fund_after -= credit
    paid_credit = credit
    used_after.append(batch_id)

# FINAL_REPORT
print("result:", result)
print("plan:", plan)
print("credit:", credit)
print("free_after:", free_after)
print("fund_after:", fund_after)
print("used_after:", used_after)
print("paid_credit:", paid_credit)

job_ids = [1, 2]
job = 1
ticket = 41
used = [40]
budget = 80
recipes = [[1, 2, 0], [0, 1, 2]]
skills = [1, 2]
minutes_by_job = [30, 40]
stock = [2, 4, 3]
part_prices = [20, 5, 10]
tech_skill = [1, 2, 1]
tech_time = [40, 60, 60]
tech_rate = [2, 1, 1]
bay_type = [1, 1, 2]
bay_time = [40, 60, 60]
bay_fee = [10, 15, 5]

# TEAM_CODE
# 01 requests
job_index = -1
required_skill = -1
minutes = 0
if ticket > 0 and ticket not in used and budget >= 0:
    for i in range(len(job_ids)):
        if job_ids[i] == job:
            job_index = i
            required_skill = skills[i]
            minutes = minutes_by_job[i]

# 02 parts
needed = []
parts_cost = 0
parts_ok = job_index != -1
for i in range(len(stock)):
    qty = 0
    if job_index != -1:
        qty = recipes[job_index][i]
    needed.append(qty)
    parts_cost += qty * part_prices[i]
    if qty > stock[i]:
        parts_ok = False

# 03 technicians
tech_candidates = []
if parts_ok:
    for i in range(len(tech_skill)):
        if tech_skill[i] == required_skill and tech_time[i] >= minutes:
            tech_candidates.append(i)

# 04 bays
pairs = []
for t in tech_candidates:
    for b in range(len(bay_type)):
        if bay_type[b] == required_skill and bay_time[b] >= minutes:
            pairs.append([t, b])

# 05 pricing
tech = -1
bay = -1
total = -1
for pair in pairs:
    t = pair[0]
    b = pair[1]
    cost = parts_cost + minutes * tech_rate[t] + bay_fee[b]
    if cost <= budget and (tech == -1 or cost < total):
        tech = t
        bay = b
        total = cost

# 06 commit
stock_after = []
tech_after = []
bay_after = []
used_after = []
for value in stock:
    stock_after.append(value)
for value in tech_time:
    tech_after.append(value)
for value in bay_time:
    bay_after.append(value)
for value in used:
    used_after.append(value)
if job_index == -1:
    result = "REQUEST"
elif not parts_ok:
    result = "PARTS"
elif len(tech_candidates) == 0:
    result = "TECH"
elif len(pairs) == 0:
    result = "BAY"
elif tech == -1:
    result = "BUDGET"
else:
    result = "OK"
    for i in range(len(needed)):
        stock_after[i] -= needed[i]
    tech_after[tech] -= minutes
    bay_after[bay] -= minutes
    used_after.append(ticket)

# FINAL_REPORT
print("result:", result)
print("tech:", tech)
print("bay:", bay)
print("total:", total)
print("stock_after:", stock_after)
print("tech_after:", tech_after)
print("bay_after:", bay_after)
print("used_after:", used_after)

members = [101, 102]
active = [True, True]
levels = [1, 2]
credits = [150, 90]
discounted = [True, False]
busy = [[False, True, False, False], [False, False, False, False]]
person = 101
registration = 61
used = [60]
activity = 1
course_activity = [1, 1, 1, 2]
course_level = [1, 1, 2, 1]
course_slots = [[0, 1], [2, 3], [0, 2], [1]]
seats = [2, 3, 1, 4]
prices = [60, 80, 70, 30]

# TEAM_CODE
# 01 members
member = -1
level = -1
if registration > 0 and registration not in used:
    for i in range(len(members)):
        if members[i] == person and active[i]:
            member = i
            level = levels[i]

# 02 catalog
course_candidates = []
if member != -1:
    for i in range(len(course_activity)):
        if course_activity[i] == activity and course_level[i] <= level:
            course_candidates.append(i)

# 03 schedule
time_candidates = []
for i in course_candidates:
    ok = True
    for slot in course_slots[i]:
        if busy[member][slot]:
            ok = False
    if ok:
        time_candidates.append(i)

# 04 capacity
seat_candidates = []
for i in time_candidates:
    if seats[i] > 0:
        seat_candidates.append(i)

# 05 pricing
course = -1
total = -1
for i in seat_candidates:
    cost = prices[i]
    if discounted[member]:
        cost -= 10
        if cost < 0:
            cost = 0
    if cost <= credits[member] and (course == -1 or cost < total):
        course = i
        total = cost

# 06 commit
busy_after = []
seats_after = []
credits_after = []
used_after = []
for line in busy:
    copy = []
    for flag in line:
        copy.append(flag)
    busy_after.append(copy)
for value in seats:
    seats_after.append(value)
for value in credits:
    credits_after.append(value)
for value in used:
    used_after.append(value)
if member == -1:
    result = "MEMBER"
elif len(course_candidates) == 0:
    result = "COURSE"
elif len(time_candidates) == 0:
    result = "TIME"
elif len(seat_candidates) == 0:
    result = "SEAT"
elif course == -1:
    result = "CREDIT"
else:
    result = "OK"
    for slot in course_slots[course]:
        busy_after[member][slot] = True
    seats_after[course] -= 1
    credits_after[member] -= total
    used_after.append(registration)

# FINAL_REPORT
print("result:", result)
print("course:", course)
print("total:", total)
print("busy_after:", busy_after)
print("seats_after:", seats_after)
print("credits_after:", credits_after)
print("used_after:", used_after)

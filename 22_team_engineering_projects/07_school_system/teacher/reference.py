groups = [11, 22]
sizes = [28, 20]
group = 11
subject = "python"
teacher_subjects = ["python", "python", "math"]
teacher_quota = [2, 1, 3]
teacher_free = [[False, True, True], [True, False, True], [True, True, True]]
room_caps = [24, 30, 40]
room_free = [[True, True, True], [False, True, True], [True, True, False]]
group_free = [[True, True, True], [True, False, True]]
group_quota = [2, 2]

# TEAM_CODE
# 01 groups
g = -1
size = 0
for i in range(len(groups)):
    if groups[i] == group and sizes[i] > 0:
        g = i
        size = sizes[i]

# 02 teachers
teacher_candidates = []
if g != -1:
    for i in range(len(teacher_subjects)):
        if teacher_subjects[i] == subject and teacher_quota[i] > 0:
            teacher_candidates.append(i)

# 03 rooms
room_candidates = []
if g != -1:
    for i in range(len(room_caps)):
        if room_caps[i] >= size:
            room_candidates.append(i)

# 04 schedule
slot = -1
teacher = -1
room = -1
if g != -1:
    for s in range(len(group_free[g])):
        if slot == -1 and group_free[g][s]:
            candidate_teacher = -1
            candidate_room = -1
            for t in teacher_candidates:
                if candidate_teacher == -1 and teacher_free[t][s]:
                    candidate_teacher = t
            for r in room_candidates:
                if room_free[r][s]:
                    if candidate_room == -1 or room_caps[r] < room_caps[candidate_room]:
                        candidate_room = r
            if candidate_teacher != -1 and candidate_room != -1:
                slot = s
                teacher = candidate_teacher
                room = candidate_room

# 05 curriculum
quota_ok = False
proposed_quota = -1
if slot != -1 and group_quota[g] > 0:
    quota_ok = True
    proposed_quota = group_quota[g] - 1

# 06 registrar
teacher_after = []
room_after = []
group_after = []
tquota_after = []
gquota_after = []
for line in teacher_free:
    row_copy = []
    for value in line:
        row_copy.append(value)
    teacher_after.append(row_copy)
for line in room_free:
    row_copy = []
    for value in line:
        row_copy.append(value)
    room_after.append(row_copy)
for line in group_free:
    row_copy = []
    for value in line:
        row_copy.append(value)
    group_after.append(row_copy)
for value in teacher_quota:
    tquota_after.append(value)
for value in group_quota:
    gquota_after.append(value)
if g == -1:
    result = "GROUP"
elif len(teacher_candidates) == 0:
    result = "TEACHER"
elif len(room_candidates) == 0:
    result = "ROOM"
elif slot == -1:
    result = "TIME"
elif not quota_ok:
    result = "QUOTA"
else:
    result = "OK"
    teacher_after[teacher][slot] = False
    room_after[room][slot] = False
    group_after[g][slot] = False
    tquota_after[teacher] -= 1
    gquota_after[g] = proposed_quota

# FINAL_REPORT
print("result:", result)
print("slot:", slot)
print("teacher:", teacher)
print("room:", room)
print("teacher_after:", teacher_after)
print("room_after:", room_after)
print("group_after:", group_after)
print("tquota_after:", tquota_after)
print("gquota_after:", gquota_after)

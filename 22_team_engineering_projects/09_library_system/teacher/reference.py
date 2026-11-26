members = [101, 102]
active = [True, True]
limits = [2, 1]
reader = 101
loan_id = 51
used_ids = [50]
book_ids = [10, 20]
book = 10
copy_books = [10, 10, 10, 20]
holders = [0, 0, 0, 0]
reserved = [102, 0, 101, 0]
distances = [1, 5, 3, 2]
day = 10

# TEAM_CODE
# 01 members
member = -1
if loan_id > 0 and loan_id not in used_ids:
    for i in range(len(members)):
        if members[i] == reader and active[i]:
            member = i
member_ok = member != -1

# 02 catalog
book_ok = member_ok and book in book_ids

# 03 copies
candidates = []
if book_ok:
    for i in range(len(copy_books)):
        if copy_books[i] == book and holders[i] == 0 and (reserved[i] == 0 or reserved[i] == reader):
            candidates.append(i)

# 04 selection
copy_index = -1
for i in candidates:
    if copy_index == -1 or distances[i] < distances[copy_index]:
        copy_index = i

# 05 policy
limit_ok = False
due = -1
if copy_index != -1 and limits[member] > 0:
    limit_ok = True
    period = 14
    if distances[copy_index] > 3:
        period = 7
    due = day + period

# 06 commit
holders_after = []
reserved_after = []
limits_after = []
used_after = []
for value in holders:
    holders_after.append(value)
for value in reserved:
    reserved_after.append(value)
for value in limits:
    limits_after.append(value)
for value in used_ids:
    used_after.append(value)
if not member_ok:
    result = "MEMBER"
elif not book_ok:
    result = "BOOK"
elif copy_index == -1:
    result = "COPY"
elif not limit_ok:
    result = "LIMIT"
else:
    result = "OK"
    holders_after[copy_index] = reader
    reserved_after[copy_index] = 0
    limits_after[member] -= 1
    used_after.append(loan_id)

# FINAL_REPORT
print("result:", result)
print("copy_index:", copy_index)
print("due:", due)
print("holders_after:", holders_after)
print("reserved_after:", reserved_after)
print("limits_after:", limits_after)
print("used_after:", used_after)

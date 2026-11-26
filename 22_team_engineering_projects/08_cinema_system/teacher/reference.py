movie_ids = [10, 20]
durations = [90, 100]
movie = 10
booking_code = 11
used_codes = [7, 8]
group_size = 3
show_movies = [10, 10, 20]
show_starts = [100, 120, 110]
earliest_start = 100
closing = 240
halls = [[[0, 0, 7, 0], [7, 0, 8, 0]], [[0, 0, 0, 8], [7, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]
ticket_prices = [30, 35, 40]
paid = 100

# TEAM_CODE
# 01 catalog
movie_index = -1
for i in range(len(movie_ids)):
    if movie_ids[i] == movie:
        movie_index = i
request_ok = movie_index != -1 and booking_code > 0 and booking_code not in used_codes and group_size > 0
length = 0
if request_ok:
    length = durations[movie_index]

# 02 screenings
show_candidates = []
if request_ok:
    for i in range(len(show_movies)):
        if show_movies[i] == movie and show_starts[i] >= earliest_start and show_starts[i] + length <= closing:
            show_candidates.append(i)

# 03 seats
show = -1
row_index = -1
start_col = -1
for candidate in show_candidates:
    found_row = -1
    found_col = -1
    for r in range(len(halls[candidate])):
        streak = 0
        for c in range(len(halls[candidate][r])):
            if halls[candidate][r][c] == 0:
                streak += 1
                if found_row == -1 and streak >= group_size:
                    found_row = r
                    found_col = c - group_size + 1
            else:
                streak = 0
    if found_row != -1:
        if show == -1 or show_starts[candidate] < show_starts[show]:
            show = candidate
            row_index = found_row
            start_col = found_col

# 04 pricing
total = -1
discount = 0
if show != -1:
    if group_size >= 3:
        discount = group_size * 5
    total = group_size * ticket_prices[show] - discount

# 05 payments
payment_ok = total >= 0 and paid >= total
change_proposed = 0
if payment_ok:
    change_proposed = paid - total

# 06 booking
halls_after = []
for hall in halls:
    hall_copy = []
    for row in hall:
        row_copy = []
        for seat in row:
            row_copy.append(seat)
        hall_copy.append(row_copy)
    halls_after.append(hall_copy)
used_after = []
for code in used_codes:
    used_after.append(code)
revenue = 0
refund = paid
if not request_ok:
    result = "REQUEST"
elif len(show_candidates) == 0:
    result = "SHOW"
elif show == -1:
    result = "SEATS"
elif not payment_ok:
    result = "PAYMENT"
else:
    result = "OK"
    for offset in range(group_size):
        halls_after[show][row_index][start_col + offset] = booking_code
    used_after.append(booking_code)
    revenue = total
    refund = change_proposed

# FINAL_REPORT
print("result:", result)
print("show:", show)
print("row_index:", row_index)
print("start_col:", start_col)
print("total:", total)
print("discount:", discount)
print("revenue:", revenue)
print("refund:", refund)
print("used_after:", used_after)
print("halls_after:", halls_after)

player_ids = [101, 102]
rows = [1, 2]
cols = [0, 0]
energies = [5, 10]
scores = [20, 5]
grid = [[0, 3, -1, 0], [0, 2, 0, 3], [0, 0, -1, 0]]
player = 101
direction = 2

# TEAM_CODE
# 01 players
index = -1
for i in range(len(player_ids)):
    if player_ids[i] == player:
        index = i
row_now = -1
col_now = -1
energy_now = -1
score_now = -1
if index != -1:
    row_now = rows[index]
    col_now = cols[index]
    energy_now = energies[index]
    score_now = scores[index]

# 02 movement
direction_ok = index != -1 and direction >= 1 and direction <= 4
nr = -1
nc = -1
if direction_ok:
    nr = row_now
    nc = col_now
    if direction == 1:
        nr -= 1
    elif direction == 2:
        nc += 1
    elif direction == 3:
        nr += 1
    else:
        nc -= 1

# 03 obstacles
motion_status = "SKIP"
energy_after_move = energy_now
tile = 0
if direction_ok:
    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]):
        motion_status = "OUTSIDE"
    elif grid[nr][nc] == -1:
        motion_status = "BLOCKED"
    elif energy_now < 2:
        motion_status = "ENERGY"
    else:
        motion_status = "OK"
        energy_after_move -= 2
        tile = grid[nr][nc]

# 04 items
energy_proposed = energy_after_move
item_points = 0
picked = False
if motion_status == "OK":
    if tile == 2:
        energy_proposed += 3
        if energy_proposed > 10:
            energy_proposed = 10
        picked = True
    elif tile == 3:
        item_points = 10
        picked = True

# 05 score
score_proposed = score_now
if motion_status == "OK":
    score_proposed += 1 + item_points
next_level = -1
if score_now >= 0:
    next_level = 1 + score_proposed // 10

# 06 engine
rows_after = []
cols_after = []
energies_after = []
scores_after = []
grid_after = []
for i in range(len(rows)):
    rows_after.append(rows[i])
    cols_after.append(cols[i])
    energies_after.append(energies[i])
    scores_after.append(scores[i])
for line in grid:
    row_copy = []
    for value in line:
        row_copy.append(value)
    grid_after.append(row_copy)
if index == -1:
    result = "PLAYER"
elif not direction_ok:
    result = "DIRECTION"
elif motion_status != "OK":
    result = motion_status
else:
    result = "OK"
    rows_after[index] = nr
    cols_after[index] = nc
    energies_after[index] = energy_proposed
    scores_after[index] = score_proposed
    if picked:
        grid_after[nr][nc] = 0

# FINAL_REPORT
print("result:", result)
print("next_level:", next_level)
print("rows_after:", rows_after)
print("cols_after:", cols_after)
print("energies_after:", energies_after)
print("scores_after:", scores_after)
print("grid_after:", grid_after)

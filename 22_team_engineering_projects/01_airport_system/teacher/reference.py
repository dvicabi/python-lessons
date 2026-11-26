flight_ids = [41, 42]
flight_caps = [5, 8]
booked = [5, 7]
flight_times = [30, 40]
requested = 41
checked = 5
bag_weights = [10, 12, 8, 15]
gate_sizes = [8, 5, 6]
gate_busy = [False, False, True]
now = 20

# TEAM_CODE
# 01 flights
flight_index = -1
for i in range(len(flight_ids)):
    if flight_ids[i] == requested:
        flight_index = i
flight_ok = flight_index != -1
capacity = -1
expected_passengers = -1
flight_time = -1
if flight_ok:
    capacity = flight_caps[flight_index]
    expected_passengers = booked[flight_index]
    flight_time = flight_times[flight_index]

# 02 passengers
passenger_ready = flight_ok and checked > 0 and checked == expected_passengers and checked <= capacity
approved_count = 0
if passenger_ready:
    approved_count = checked

# 03 baggage
bag_total = 0
bag_ready = passenger_ready and len(bag_weights) <= approved_count
for weight in bag_weights:
    bag_total += weight
    if weight < 1 or weight > 20:
        bag_ready = False
if bag_total > approved_count * 15:
    bag_ready = False

# 04 gates
gate_index = -1
if passenger_ready and bag_ready:
    for i in range(len(gate_sizes)):
        if not gate_busy[i] and gate_sizes[i] >= approved_count:
            if gate_index == -1 or gate_sizes[i] < gate_sizes[gate_index]:
                gate_index = i

# 05 schedule
ready_at = -1
slot_ok = False
if gate_index != -1:
    ready_at = now + approved_count + bag_total // 10
    slot_ok = ready_at <= flight_time

# 06 controller
gate_busy_after = []
for busy in gate_busy:
    gate_busy_after.append(busy)
departed_id = -1
if not flight_ok:
    result = "FLIGHT"
elif not passenger_ready:
    result = "PASSENGERS"
elif not bag_ready:
    result = "BAGS"
elif gate_index == -1:
    result = "GATE"
elif not slot_ok:
    result = "TIME"
else:
    result = "OK"
    gate_busy_after[gate_index] = True
    departed_id = requested

# FINAL_REPORT
print("flight_ok:", flight_ok)
print("passenger_ready:", passenger_ready)
print("bag_ready:", bag_ready)
print("gate_index:", gate_index)
print("ready_at:", ready_at)
print("slot_ok:", slot_ok)
print("result:", result)
print("gate_busy_after:", gate_busy_after)
print("departed_id:", departed_id)

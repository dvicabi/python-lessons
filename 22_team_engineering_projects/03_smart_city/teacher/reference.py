districts = [11, 22]
district = 11
water_need = 4
base_power = 8
trips = 3
cars = 2
water_available = [10, 8]
power_available = [24, 15]
bus_district = [11, 11, 22]
bus_free = [5, 3, 6]
parking_free = [3, 5]

# TEAM_CODE
# 01 requests
d = -1
for i in range(len(districts)):
    if districts[i] == district:
        d = i
request_ok = d != -1 and water_need >= 0 and base_power >= 0 and trips >= 0 and cars >= 0 and water_need + base_power + trips + cars > 0
if not request_ok:
    d = -1

# 02 water
water_ok = False
pump_power = 0
if request_ok and water_need <= water_available[d]:
    water_ok = True
    pump_power = water_need * 2

# 03 power
power_need = 0
power_ok = False
if water_ok:
    power_need = base_power + pump_power + trips * 2
    power_ok = power_need <= power_available[d]

# 04 transit
bus = -1
transit_ok = False
if power_ok:
    if trips == 0:
        transit_ok = True
    else:
        for i in range(len(bus_free)):
            if bus_district[i] == district and bus_free[i] >= trips:
                if bus == -1 or bus_free[i] < bus_free[bus]:
                    bus = i
        transit_ok = bus != -1

# 05 parking
parking_ok = False
parking_left = -1
if transit_ok and cars <= parking_free[d]:
    parking_ok = True
    parking_left = parking_free[d] - cars

# 06 controller
water_after = []
power_after = []
bus_after = []
parking_after = []
for value in water_available:
    water_after.append(value)
for value in power_available:
    power_after.append(value)
for value in bus_free:
    bus_after.append(value)
for value in parking_free:
    parking_after.append(value)
if not request_ok:
    result = "REQUEST"
elif not water_ok:
    result = "WATER"
elif not power_ok:
    result = "POWER"
elif not transit_ok:
    result = "TRANSIT"
elif not parking_ok:
    result = "PARKING"
else:
    result = "OK"
    water_after[d] -= water_need
    power_after[d] -= power_need
    if bus != -1:
        bus_after[bus] -= trips
    parking_after[d] = parking_left

# FINAL_REPORT
print("result:", result)
print("power_need:", power_need)
print("bus:", bus)
print("water_after:", water_after)
print("power_after:", power_after)
print("bus_after:", bus_after)
print("parking_after:", parking_after)

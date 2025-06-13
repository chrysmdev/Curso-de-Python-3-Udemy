"""
CONSTANT = "Variables" that do not change
Too many conditions in the same if (bad)
    <- Complexity count (bad)
"""

speed = 61  # current speed of the car
car_local = 90  # location where the car is on the road

RADAR_1 = 60  # maximum speed of radar 1
LOCAL_1 = 100  # location where the radar 1
RADAR_RANGE = 1  # The distance where the radar picks up

car_speed_pass_radar_1 = speed > RADAR_1
car_passed_radar_1 = car_local >= (LOCAL_1 - RADAR_RANGE) and car_local <= (
    LOCAL_1 + RADAR_RANGE
)
car_fined_radar_1 = car_passed_radar_1 and car_speed_pass_radar_1

if car_speed_pass_radar_1 > RADAR_1:
    print("'The car's speed exceeded radar 1")

if car_passed_radar_1:
    print("Car passed radar 1")

if car_fined_radar_1:
    print("Car fined by radar 1")

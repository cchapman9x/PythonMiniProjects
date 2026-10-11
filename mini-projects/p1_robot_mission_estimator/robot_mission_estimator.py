'''
Project: Robot Mission Estimator
Date: 10/10/2026
Name: Caleb Chapman

Description: The 'Robot Mission Estimator' is a small terminal program that estimates 
whether a robot has enough battery to complete a trip.
'''

import time
import rme_functions
import lib1_basic_math as bm

"""
r (r before """ """) -  The 'r' prefix makes a string a raw string, which treats 
backslashes as literal characters instead of escape sequences. This makes it great 
for adding multiline ASCII code to your programs.
""" 

PROGRAM_TITLE = r"""
 _____       _           _     __  __ _         _               ______     _   _                 _             
|  __ \     | |         | |   |  \/  (_)       (_)             |  ____|   | | (_)               | |            
| |__) |___ | |__   ___ | |_  | \  / |_ ___ ___ _  ___  _ __   | |__   ___| |_ _ _ __ ___   __ _| |_ ___  _ __ 
|  _  // _ \| '_ \ / _ \| __| | |\/| | / __/ __| |/ _ \| '_ \  |  __| / __| __| | '_ ` _ \ / _` | __/ _ \| '__|
| | \ \ (_) | |_) | (_) | |_  | |  | | \__ \__ \ | (_) | | | | | |____\__ \ |_| | | | | | | (_| | || (_) | |   
|_|  \_\___/|_.__/ \___/ \__| |_|  |_|_|___/___/_|\___/|_| |_| |______|___/\__|_|_| |_| |_|\__,_|\__\___/|_|
_______________________________________________________________________________________________________________
 """

print(PROGRAM_TITLE)

# 1. Ask for robot's name
robot_name = input("Enter Robot Name: ")
# 2. Available battery energy in watt-hours (Wh)
battery_lvl = float(input(f"Enter {robot_name}'s Battery Energy Level in watt-hours(Wh): "))
# 3. Average power consumption in watts (W)
power_consumption = float(input(f"Enter {robot_name}'s Power Consumption in watts(W): "))
# 4. Movement speed in meters per second (m/s) 
movement_speed = float(input(f"Enter {robot_name}'s movement speed in meters per second(m/s): "))
# 5. Total planned travel distance in meters (m)
total_planned_distance = float(input(f"Enter {robot_name}'s planned travel distance in meters(m): "))

# Calculating Animation
for i in range(0, 3):
    print("\n Calculating...")
    time.sleep(2)

print("_______________________________________________________________________________________________________________\n")

# 6. Calculate Runtime in hours
runtime = rme_functions.runtime_in_hours(battery_lvl, power_consumption) # in hours

# 8. Calculate Maximum Distance in meters of the robot
# Convert runtime to seconds first
runtime_in_seconds = bm.hours_to_seconds(runtime)
max_distance = rme_functions.maximum_distance(movement_speed, runtime_in_seconds)

# 7. Calculate Trip Time in seconds
trip_duration = rme_functions.trip_time(total_planned_distance, movement_speed)

# 8. Then print a report with those results and a Boolean showing 
# whether the maximum distance is enough for the trip
print("Estimations Report:\n")

print(f">>> {robot_name}'s Runtime: {runtime} hours")
print(f">>> {robot_name}'s Travel Distance Capacity: {max_distance} meters")
print(f">>> Trip Duration Based on {robot_name}'s movement speed: {trip_duration} seconds\n")

if max_distance >= total_planned_distance:
    print(f">>> Mission Possible: True")
    print(f"{robot_name} has enough power to make the journey\n")
elif max_distance <= total_planned_distance:
    print(f">>> Mission Possible: False")
    print(f"{robot_name} does not have enough power to make the journey\n")

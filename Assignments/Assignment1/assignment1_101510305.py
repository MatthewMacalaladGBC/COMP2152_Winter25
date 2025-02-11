"""
AUTHOR: Matthew Macalalad
Assignment: #1
"""

gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5 # Float
highest_reps = 25 # Integer
membership_active = True # Boolean

# Dictionary: A data type in which each entry consists of a colon-separated pair; a key and a value, with the key acting as an index. 
workout_stats = {"Alex" : (30, 45, 20), "Jamie" : (30, 25, 35), "Taylor" : (35, 40, 45)}
# key = "Name" : value = (yoga time, running time, weightlifting time)
workout_totals = {} # Empty dictionary to add total workout minutes to

for key, value in workout_stats.items():
    total_minutes = sum(value)
    workout_totals[key + "_Total"] = total_minutes

# List: A data type that can hold a collection of objects. The elements of the list do not all have to be the same type.
workout_list = [list(value) for value in workout_stats.values()]
print("Yoga and running minutes for all friends in records: " + " | ".join(f"{time[:2]}" for time in workout_list))
print("Weightlifting minutes for last two friends in records: " + " | ".join(f"{time[2:]}" for time in workout_list[1:]))

for key, value in workout_stats.items():
    if sum(value) >= 120:
        print(f"Great job staying active, {key}!")

entered_name = input("Enter a friend's name to see their workout stats: ")

# Loops through workout_stats to find entered_name, then prints their workout stats if found
if entered_name in workout_stats:
    print(f"{entered_name} has the following workout stats: ")
    print(f"Yoga - {workout_stats[entered_name][0]} minutes.")
    print(f"Running - {workout_stats[entered_name][1]} minutes.")
    print(f"Weightlifting - {workout_stats[entered_name][2]} minutes.")
    print(f"Total workout minutes - {workout_totals[entered_name + '_Total']} minutes.")
else:
    print(f"Friend {entered_name} not found in the records.")

max_val = max(workout_totals.values()) # Finds highest total minutes using max() function on workout_totals
max_name = [key for key, value in workout_stats.items() if sum(value) == max_val][0] # Returns key of friend with highest total minutes, to get name (without "_Total")
                                                                                     # from workout_stats by comparing sum of values with found max_value
print(f"The friend with the most total workout minutes is {max_name} with {max_val} minutes.")

# Same logic as above, but using min() function to find lowest total minutes
min_val = min(workout_totals.values())
min_name = [key for key, value in workout_stats.items() if sum(value) == min_val][0]
print(f"The friend with the least total workout minutes is {min_name} with {min_val} minutes.")


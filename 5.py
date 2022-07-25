import os
import time    

# Countdown function
def countdown():
    
    # Function to output that the value is invalid
    def invalidval():
        print("Invalid Value!")
        return countdown()
    
    # Time input
    try:
        time_d = int(input("Please enter time in days: "))
        time_h = int(input("Please enter time in hours: "))
        time_m = int(input("Please enter time in minutes: "))
        time_s = int(input("Please enter time in seconds: "))
    except ValueError:
        invalidval()
    
    if time_d < 0 or time_h < 0 or time_m < 0 or time_s < 0:
        invalidval()
    
    # Counting down Function
    def count(time_d, time_h, time_m, time_s):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("{}d, {}h, {}m, {}s".format(time_d, time_h, time_m, time_s))
        time.sleep(1)
        if time_s > 0:
            time_s -= 1
            return count(time_d, time_h, time_m, time_s)
        elif time_m > 0:
            time_m -= 1
            time_s += 59
            return count(time_d, time_h, time_m, time_s)
        elif time_h > 0:
            time_h -= 1
            time_m += 59
            time_s += 59
            return count(time_d, time_h, time_m, time_s)
        elif time_d > 0:
            time_d -= 1
            time_h += 23
            time_m += 59
            time_s += 59
            return count(time_d, time_h, time_m, time_s)
        else:
            print("Finished!")
            exit()
                        
    count(time_d, time_h, time_m, time_s)

countdown()
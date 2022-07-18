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
        
    # Summary time to count down
    time_total = time_s + time_m * 60 + time_h * 3600 + time_d * 86400
    
    # Counting down Function
    def count(time_total):
        if time_total != 0:
            os.system('clear')
            print(time_total)
            time_total -= 1
            time.sleep(1)
            return count(time_total)
        else:
            os.system('clear')
            print("Finished!")
            exit()
    count(time_total)

countdown()
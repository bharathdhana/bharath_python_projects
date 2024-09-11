#Creating a tuple for representing time in hour and minutes
import datetime as dt
current_time = dt.datetime.now()
print(current_time)
#print(f"Hours:{time.hour} Minute:{time.minute}")

time_tuple = (current_time.hour, current_time.minute)
print("Time tuple (hour, minute):", time_tuple)

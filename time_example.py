import time

# 1. Get the current time in seconds 
# since the epoch (January 1, 1970)
current_time = time.time()
print(f"Current time in seconds since epoch: {current_time}")

# 2. Convert the time in seconds to a readable format
local_time = time.ctime(current_time)
print(f"Local time: {local_time}")

# 3. Pause the program for 2 seconds
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake!")

# 5. Measure the execution time of a piece of code
start_time = time.time()
# Simulate some processing with a sleep
time.sleep(1)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

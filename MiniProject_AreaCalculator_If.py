import time

#request info and time
event_type = input("Enter the type of event - swimming, cycling, or running: ")
start_time= time.time()

#timer to stop to have final time
timer = input("Press anything to stop")
#time differences in seconds
end_time=time.time()-start_time

# convert second to minutes
end_time  = end_time/60

if end_time <= 100: 
    print(f"{event_type} - Provincial Colours")

elif end_time <= 105:
    print(f"{event_type} - Provincial Half Colours")

elif end_time <= 110:
    print(f"{event_type} - Provincial Scroli")

else:
    print(f"{event_type} - No award")


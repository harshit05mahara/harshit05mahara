import time 
tt=time.strftime('%H:%M:%S')
print(tt)
hour=int(time.strftime('%H'))
# print("hour:",hour)
if 1<hour<12:
    print("Hey Good morning sir !!")
elif 12<=hour<=16:
    print("Hey Good afternoon sir !")
elif 16<=hour<24:
    print("Hey Good evening sir")
else:
    print("Good evening sir")
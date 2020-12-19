import datetime
import time

def countdown_timer(t):
    while t > 0 :
        time_left = datetime.timedelta(seconds=t).seconds
        print("剩下%s秒可以回答!加快速度!" % time_left)
        print("\n")
        t -= 1
        time.sleep(1)
    print("時間到!換下一題囉~")

countdown_timer(10)

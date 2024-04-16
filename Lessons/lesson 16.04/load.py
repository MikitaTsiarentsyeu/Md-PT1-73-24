import time_it
import time_it_inc

timer = time_it.Time_it()
timer2 = time_it.Time_it()
print(time_it_inc.__dict__)

total = 0

time_it_inc.start()
timer.start()
for i in range(10):
    timer2.start()
    for j in range(100000):
        i + j
    res = timer2.finish()
    total += res

res = timer.finish()
res2 = time_it_inc.finish()
print(res, total, res2)
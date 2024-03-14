import time_it_package.time_it as ti

ti.start()
for i in range(1000000):
    i+=1
res = ti.finish()

print(res)
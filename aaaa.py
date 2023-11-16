from alive_progress import alive_bar; import time
import sys
print("ERROR RELOAD THE SYS")
time.sleep(1)
print("RELOADING SYS PLEASE WAIT")

for total in 5000, 7000, 4000, 0:
    with alive_bar(total) as bar:
        for _ in range(5000):
            time.sleep(.001)
            bar()

print("SYS RELOADED")
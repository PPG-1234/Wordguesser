from sys import stdout
import time
def slow(x,t,end=True):
    for i in x:
        stdout.write(i)
        stdout.flush()
        time.sleep(t)
    if end:print()

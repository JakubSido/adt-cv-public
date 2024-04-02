
import time
def measure_time(func,ntimes=1,pause=0.01):
    start = time.time()
    ret = None
    for _ in range(ntimes):
        ret = func()
        time.sleep(pause)
    dur = time.time() - start
    print(f"Duration: {((dur-(ntimes*pause))/ntimes)*1000}ms")
    return ret

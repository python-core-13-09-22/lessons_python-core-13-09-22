
import random
import time
from multiprocessing import Pool




def my_print(index):

    print(f"start my_print_{index}")
    seconds = random.randint(0, 3)
    time.sleep(seconds)
    print(f"end my_print_{index} sleep {seconds}s")
    return  seconds

if __name__ == '__main__':
    time_start = time.time()
    vals = [i for i in range(100)]
    with Pool(15) as pool:
        res = pool.map(my_print, vals)
    time_end = time.time()
    print(f"runs {time_end - time_start}s")
    print(f"all time {sum(res)}")

# python quickMergeSort.py


import random
import time
from mergesort import merge_sort
from timsort import tim_sort
from quicksort import quick_sort

def quicksort_vs_mergesort():
    data = []

    for i in range(4000000):
        random_num = random.randint(0, 4000000)
        data.append(random_num)

    start = time.time()
    quick_sort(data, 0, len(data) - 1)
    end = time.time()
    print("[QUICKSORT] 4000000 (4 million) integers random numbers \n [start] "+ str(end - start))
    print("\n")
    
    data = []

    for i in range(4000000):
        random_num = random.randint(0, 4000000)
        data.append(random_num)

    start = time.time()
    merge_sort(data)
    end = time.time()
    print("[MERGESORT] 4000000 (4 million) integers random numbers \n [start] "+ str(end - start))
    print("\n")



if __name__ == "__main__":
    quicksort_vs_mergesort()
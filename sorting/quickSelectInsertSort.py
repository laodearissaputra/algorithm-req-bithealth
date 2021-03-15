# python quickSelectInsertSort.py


import random
import time
from selectionsort import selection_sort
from insertionsort import insertion_sort
from quicksort import quick_sort

def quick_vs_selec_vs_insr():
    data = []

    for i in range(40000):
        random_num = random.randint(0, 40000)
        data.append(random_num)
    
    start = time.time()
    quick_sort(data, 0, len(data) - 1)
    end = time.time()
    print("[QUICKSORT] 40000 (40K) integers random numbers \n [start] "+ str(end - start))
    print("\n")
    
    data = []

    for i in range(40000):
        random_num = random.randint(0, 40000)
        data.append(random_num)
    
    start = time.time()
    selection_sort(data, len(data))
    end = time.time()
    print("[SELECTIONSORT] 40000 (40 mil) integers random_nums\n[start] "+ str(end - start))
    print("\n")
    
    data = []

    for i in range(40000):
        random_num = random.randint(0, 40000)
        data.append(random_num)

    start = time.time()
    insertion_sort(data, len(data))
    end = time.time()
    print("[INSERTIONSORT] 40000 (40 mil) integers random numbers \n[start] "+ str(end - start))
    print("\n")

if __name__ == "__main__":
    quick_vs_selec_vs_insr()
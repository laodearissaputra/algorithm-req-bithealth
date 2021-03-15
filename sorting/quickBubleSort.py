# python quickBubleSort.py


import random
import time
from bubblesort import bubble_sort
from quicksort import quick_sort

def quicksort_vs_bubble():
    lista = []

    for i in range(40000):
        random_num = random.randint(0, 40000)
        lista.append(random_num)

    start = time.time()
    quick_sort(lista, 0, len(lista) - 1)
    end = time.time()
    print("[QUICKSORT] 40000 (40K) integers random numbers \n [TIME] "+ str(end - start))
    
    lista = []

    for i in range(40000):
        random_num = random.randint(0, 40000)
        lista.append(random_num)

    start = time.time()
    bubble_sort(lista, len(lista))
    end = time.time()
    print("[BUBBLESORT] 40000 (40K) integers random numbers \n [TIME] "+ str(end - start))
    
    print("\n")

if __name__ == "__main__":
    quicksort_vs_bubble()

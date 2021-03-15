# python sortAverageTest.py

import random
import time
from quicksort import quick_sort

def quicksort_average():
    def test1():
        data = []

        for i in range(40000):
            random_num = random.randint(0, 40000)
            data.append(random_num)

        start = time.time()
        quick_sort(data, 0, len(data) - 1)
        end = time.time()
        print("[TEST] 40,000 (40,000) integers \n [start] "+ str(end - start))
        print("\n")

    def test2():
        data = []

        for i in range(400000):
            random_num = random.randint(0, 400000)
            data.append(random_num)

        start = time.time()
        quick_sort(data, 0, len(data) - 1)
        end = time.time()
        print("[TEST] 400000 (400K) integers \n [start] "+ str(end - start))
        print("\n")
    
    def test3():
        data = []

        for i in range(4000000):
            random_num = random.randint(0, 4000000)
            data.append(random_num)

        start = time.time()
        quick_sort(data, 0, len(data) - 1)
        end = time.time()
        print("[TESTE] [TEST] 4000000 (4 million) whole \n [start] "+ str(end - start))
        print("\n")

    def test4():
        data = []

        for i in range(40000000):
            random_num = random.randint(0, 40000000)
            data.append(random_num)

        start = time.time()
        quick_sort(data, 0, len(data) - 1)
        end = time.time()
        print("[TEST] 40000000 (40 million) whole \n [start] "+ str(end - start))
        print("\n")

    print("Test with random numbers - general case - O (n log (n))\n")
    print("Test1: \n")
    test1()
    print("Test2: \n")
    test2()
    print("Test3: \n")
    test3()
    print("Test4: \n")
    test4()
    print("end of test")

if __name__ == "__main__":
    quicksort_average()
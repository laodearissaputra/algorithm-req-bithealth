# python quicksortTest.py

import random
import time
from quicksort import quick_sort

def quicksort_test():
    def test1():
        data =[]

        for i in range(400000):
            data.append(i)
        
        start = time.time()
        quick_sort(data, 0, len(data) - 1)
        end = time.time()
        print("[TEST] 400000 (400K) integers \ n [TIME] "+ str(end - start))
        print("\n")

    def test2():
        data = []

        for i in range(4000000):
            data.append(i)

        start = time.time()
        quick_sort(data, 0, len(data)-1)
        end = time.time()
        print("[TEST] 4000000 (4 million) whole \ n [TIME] "+ str(end - start))
        print("\n")

    def test3():
        data = []

        for i in range(40000000):
            data.append(i)

        start = time.time()
        quick_sort(data, 0, len(data)-1)
        end = time.time()
        print("[TEST] 400000000 (40 million) whole \ n [TIME] "+ str(end - start))
        print("\n")

    print("Testing the worst case of quicksort - O (n ^ 2) - [List already ordered]\n")
    test1()
    test2()
    test3()
    print("End of tests")

def quicksort_average():
    def teste1():
        lista = []

        for i in range(40000):
            random_num = random.randint(0, 40000)
            lista.append(random_num)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 40000 (40 mil) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    def teste2():
        lista = []

        for i in range(400000):
            random_num = random.randint(0, 400000)
            lista.append(random_num)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 400000 (400 mil) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")
    
    def teste3():
        lista = []

        for i in range(4000000):
            random_num = random.randint(0, 4000000)
            lista.append(random_num)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 4000000 (4 milhoes) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    def teste4():
        lista = []

        for i in range(40000000):
            random_num = random.randint(0, 40000000)
            lista.append(random_num)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 40000000 (40 milhoes) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    print("Teste com numeros aleatórios - caso geral - O(n log(n))\n")
    print("Teste1: \n")
    teste1()
    print("Teste2: \n")
    teste2()
    print("Teste3: \n")
    teste3()
    print("Teste4: \n")
    teste4()
    print("Fim dos testes")

if __name__ == "__main__":
    quicksort_test()
    quicksort_average()
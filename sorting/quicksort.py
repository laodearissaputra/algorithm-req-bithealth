# python quicksort.py

def partition(data, esq, dir, pivot):
    while(esq <= dir):
        while(data[esq] < pivot):
            esq+=1

        while(data[dir] > pivot):
            dir-=1

        if(esq <= dir):
            data[esq], data[dir] = data[dir], data[esq] # Swap
            esq+=1
            dir-=1

    return esq

def quick_sort(data, esq, dir):
    if(esq >= dir):
        return
    pivot = data[ int((esq + dir) / 2)]
    index = partition(data, esq, dir, pivot)
    quick_sort(data, esq, index-1)
    quick_sort(data, index, dir)


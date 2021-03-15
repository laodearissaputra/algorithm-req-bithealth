def bubble_sort(data, n):
    i = 0
    while(i < n-1):
        j = n-1
        while(j>i):
            if(data[j] < data[j - 1]):
                data[j - 1], data[j] = data[j], data[j - 1]
            j-=1
        i+=1


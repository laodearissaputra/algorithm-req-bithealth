
def insertion_sort(data, n):
    p = 1
    while(p<n):
        temp = data[p]
        j=p
        while(j>0 and temp < data[j - 1]):
            data[j] = data[j - 1] 
            j-=1
        data[j] = temp
        p+=1


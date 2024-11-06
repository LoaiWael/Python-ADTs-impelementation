# bubble sort
def bubbleSort(li):
    n=len(li)
    for i in range(n):
        for j in range(n-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li

# selection sort
def selectionSort(li):
    n=len(li)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if li[min]>li[j]:
                min=j
        li[min],li[i]=li[i],li[min]
    return li

# insertion sort
def insertionSort(li):
    n=len(li)
    for i in range(1,n):
        temp=li[i]
        j=i-1
        while (j>=0 and li[j]>temp ):
            li[j+1]=li[j]
            j-=1
        li[j+1]=temp
    return li

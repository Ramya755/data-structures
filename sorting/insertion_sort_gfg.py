def insertion_sort(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
            #it will check before elements like it starts from 8 actually when it went to 1 it will check upto 5 and put 1 at first
    return arr
print(insertion_sort([5,8,1,4,15,6]))
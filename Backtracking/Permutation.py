def Permutation(arr,start):
    if(start==len(arr)):
        print(arr)
        return
    for i in range(start,len(arr)):
        arr[start],arr[i]=arr[i],arr[start]
        Permutation(arr,start+1)
        arr[start],arr[i]=arr[i],arr[start]
Permutation(['A','B','C'],0)
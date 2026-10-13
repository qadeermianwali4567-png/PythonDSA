def subset(arr,index,sub):
    if(index==len(arr)):
        print(sub)
        return 
    sub.insert(index,arr[index])
    subset(arr,index+1,sub)
    sub.pop()
    subset(arr,index+1,sub)
subset([1,2,3],0,[])
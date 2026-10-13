def Combination(arr,sub,index,k):
    if(len(sub)==k):
        print(sub)
        return
    for i in range(index,len(arr)):
        sub.append(arr[i])
        Combination(arr,sub,i+1,k) 
        sub.pop()
Combination(['A','B','C'],[],0,2)
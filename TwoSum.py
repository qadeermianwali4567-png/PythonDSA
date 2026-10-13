arr=[2,3,4,5,6,7,8,10]
start=0
target=9
end=arr.__len__()-1
while(start!=end):
    if(arr[start]+arr[end]==target):
        print(arr[start],"+",arr[end],"=",target)
        break
    elif (arr[end]>target or arr[end]+arr[start]>target):
        end-=1
    else:
        start+=1

        

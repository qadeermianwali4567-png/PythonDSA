def TwoSum(arr,target):
    seen={}
    for i,num in enumerate(arr):
        complement=target-num
        if complement in seen:
              return [seen[complement],i]
        seen[num]=i
        print(seen)
    return []
n=TwoSum([2,4,6,7,8,3,5,9],17)
print(n)

def number(arr,first,last):
    if(first>=last):
        return 
    mid=int((first+last)/2)
   
    left=number(arr,first+1,mid)
    print("arr : ",arr," first : ",first," last : ",last," left : ",left)
    number(arr,mid+1,last)
arr=[6,3,7,4,5,8]
number(arr,0,len(arr))

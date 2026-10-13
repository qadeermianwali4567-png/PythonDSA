def Tower_of_Hanoi(n,source,destination,auxiliary):
    if(n==1):
        return print(f"Disk move {source} to {destination}")
    Tower_of_Hanoi(n-1,source,auxiliary,destination)
    print(f"Disk move {source} to {destination}")
    Tower_of_Hanoi(n-1,auxiliary,destination,source)
Tower_of_Hanoi(3,"A","C","B")
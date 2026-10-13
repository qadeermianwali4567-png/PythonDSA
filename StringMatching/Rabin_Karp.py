
def Hash(pattern):
    hash=0
    for i in range(0,len(pattern)):
        hash=(256*hash+ord(pattern[i]))%101
    return hash
def Rolling_Hash(Text,Pattern):
      n=len(Text)
      m=len(Pattern)
      p_hash=Hash(Pattern)
      t_hash=Hash(Text[:m])
      d=256
      h=1
      match=False
      for i in range(m - 1):
        h = (h * d) % 101
     
      for i in range(n-m+1):
        if(p_hash==t_hash):
            print("Hash Matched at ",i)
            for j in range(0,m):
                if(Text[i+j]!=Pattern[j]):
                    match=True
            if(match==True):
                print("Pattern Found at ",i)
        if i < n-m:
            t_hash = (d * (t_hash - ord(Text[i]) * h)+ ord(Text[i + m])) % 101
            if t_hash < 0:
                t_hash += 101


        
           
        
 
           

# def Text_Window(Text,n):
   
#     for i in range(0,len(Text)-n+1):
#         window=Text[i:n+i]
#         Hash(window)
#         print(window)
       
Rolling_Hash("ABCDEFGHIJKLMNOP","EFGH")
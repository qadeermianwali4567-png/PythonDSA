def NaivePatternMatching(T,P):
    n=len(T)
    m=len(P)
    for i in range(0,n-m+1):
        j=0
        while( j<m and T[i+j]==P[j]):
            j+=1
        if(j==m):
            print("Pattern found at ",i)
NaivePatternMatching("AABAACAADAABAABA","AABA")
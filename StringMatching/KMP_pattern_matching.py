def LSP_Array(P):
    LSP=[0]
    m=len(P)
    j=0
    i=1
    while(i<m):
        if(P[i]==P[j]):
            j+=1
            LSP.append(j)
            i+=1
        elif(P[i]!=P[j] and j>0):
            j=LSP[j-1]
        elif(P[i]!=P[j] and j==0):
            LSP.append(0)
            i+=1
        else:
            print("Nothing")
    return LSP
def KMP_pattern_searching(T,P):
    LSP=LSP_Array(P)
    n=len(T)
    m=len(P)
    j=0
    i=0
    while(i<n):
        if(T[i]==P[j]):
            i+=1
            j+=1
            if(j==m):
                print("Pattern Found at ",i-j)
                j=LSP[j-1]
        elif(T[i]!=P[j] and j>0):
            j=LSP[j-1]
        elif(T[i]!=P[j] and j==0):
            i+=1
        else:
            print("Nothing")
KMP_pattern_searching("AABAACAADAABAABA","AABAA")
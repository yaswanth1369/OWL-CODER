def subset(ind,stk,n,arr):
    if ind==n:
        print(stk)
        return
    #picking an element case
    stk.append(arr[ind])
    subset(ind+1,stk,n,arr)
    l=len(stk)
    stk.pop(l-1)
    #not picking element case
    subset(ind+1,stk,n,arr)
n=int(input())
arr=list(map(int,input().split()))
stk=[]
subset(0,stk,n,arr)

a=[]
b=[]
def encaixa(A,B):
    cont=0
    a=list(A)
    b=list(B)
    n=len(b)
    m=len(a)  
    a.reverse()
    b.reverse()
    a[0:(n-1)]
    a=a=list(a)
    if n <= m:
        for i in range(n):
            if a[i] == b[i]:
                cont=cont+1
        if cont==n:
            return True
        else:
            return False
    else:
        return False

N=int(input())
for _ in range(N):
    A, B = input().split()
    if encaixa(A, B):
        print("encaixa")
    else:
        print("nao encaixa")

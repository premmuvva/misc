def isPrime(n):
    for i in range (2,n):
        if (n%i==0):
            return False
    return True
def generate(a,b):
    l=[]
    for i in range(a,b):
        if (isPrime(i)):
            l+=[i];
    return l;
k=generate (2,25)
print(k)
nlist=[]
for i in range (2,51):
    a=0
    for j in k:
        a*=2
        if ( i%j == 0):
            a+=1
    nlist+=[a]
print(nlist)
print(nlist[35],nlist[39])

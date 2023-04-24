def figo(n):
    j = range(n)
    a = []
    if(n==1 or n==0):
        return 1
    if(n>1):
        for x in j:   
            if x == 0 or x == 1:
                a.append(1)
            if x>1:
                valor = a[x-2]+a[x-1]
                a.append(valor)
    return a

def format(a):
    txt = ''
    for x in a:
        txt = txt+str(x)+','
    return txt

print(format(figo(6))[:-1])

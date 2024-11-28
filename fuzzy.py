a=[10,20,30]
b=[20,30,40]
def mu_a(a):
    for i in range(len(a)):
        a[i]=[a[i],a[i]/(a[i]+10)]
    return a
def mu_b(b):
    for i in range(len(b)):
        b[i]=[b[i],(b[i]**2)/(b[i]**2+10**3)]
    return b

a=mu_a(a)
b=mu_b(b)
print("a is: ",a)
print("b is: ",b)

def fuzzy_union(a,b):
    c=[]
    for i in range(len(a)):
        c.append([a[i][0],max(a[i][1],b[i][1])])
    return c

c=fuzzy_union(a,b)
print("a union b is: ",c)

def fuzzy_intersection(a,b):
    c=[]
    for i in range(len(a)):
       for j in range(len(b)):
            if a[i][0]==b[j][0]:
                c.append([a[i][0],min(a[i][1],b[j][1])])
    return c
           

d=fuzzy_intersection(a,b)
print("a intersection b is: ",d)

def complement(a):  
    c=[]
    for i in range(len(a)):
        c.append([a[i][0],1-a[i][1]])
    return c

e=complement(a)
print("complement of a is: ",e)

f=complement(b)
print("complement of b is: ",f)
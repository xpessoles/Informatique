a=65
tab=[]
for i in range(1,a):
    tab.append(2**i)

tab2=[]
for i in range(1,a):
    tab2.append(2.**i)

aa=0.
for i in range(1,a-1):
    aa = aa+tab2[i]
    print(aa)



for i in range(a-10,a-1):
    print(str(tab[i]-tab2[i]))

n=1023
#print(str(2**n))
#print((2**(n-1))+2.**n)
#print(2.**n-(2**(n-1)))

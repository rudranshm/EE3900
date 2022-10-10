x=(1+5**(1/2))/2
y=(1-5**(1/2))/2
k=100
val1=0
for n in range(1,k):
    val1+=((x**(n)-y**(n))/((x-y)*(10**n)))
print(val1, "is the value of LHS till 100 iterations")
print(10/89, "is the value of RHS")
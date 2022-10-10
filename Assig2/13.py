x=(1+5**(1/2))/2
y=(1-5**(1/2))/2

a='y'
while a.lower()=='y':
    n=int(input("value of N : "))
    val1=((x**(n+1)-y**(n+1))/(x-y)) + ((x**(n-1)-y**(n-1))/(x-y))
    val2=(x**n)+(y**n)
    print(val1, "is the value of LHS")
    print(val2, "is the value of RHS")
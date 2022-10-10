x=(1+5**(1/2))/2
y=(1-5**(1/2))/2

a='y'
while a.lower()=='y':
    n=int(input("value of N : "))
    val1=((x**(n+2)-y**(n+2))/(x-y))-1
    val2=0
    for k in range (n+1):
        val2+=(x**k-y**k)/(x-y)
    print("LHS : ",val2)
    print("RHS : ",val1)
    a=input("More checks? Y/N : ")

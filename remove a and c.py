n=input("enter any string:")
l=len(n)
result=''
for i in range(l):
    if n[i]=='o' or n[i]=='c':
        print()
    else:
        result=result+n[i]
print(result)

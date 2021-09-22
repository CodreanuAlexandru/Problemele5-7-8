with open('Lista1.txt','r') as f:
    x=list(eval(f.read()))
with open('Lista2.txt','r') as f:
    y=list(eval(f.read()))
print(x[0]+x[1]+x[2])
print(sum(x))
p=1
for i in range(len(x)):
    a=x[i-1]
    p=p*a
print(p)
b=abs(y[3])
print(b)
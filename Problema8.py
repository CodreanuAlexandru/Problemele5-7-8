ore=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
with open('temperatura.txt','r') as f:
    t=list(eval(f.read()))
print(sum(t)/24)
i=0
while t[i]!=max(t):
    i+=1
print('Maximum la ora',ore[i],'cu temperatura',t[i])
z=0
while t[z]!=min(t):
    z+=1
print('Minimul la ora',ore[z],'cu temperatura',t[z])
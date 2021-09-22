zi=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
with open('Venit.txt','r')as f:
    v=list(eval(f.read()))
print(sum(v))
print(sum(v)/7)
i=0
while v[i]!=max(v):
    i+=1
z=0
while v[z]!=min(v):
    z+=1
print(zi[i],'are venit maxim de',v[i])
print(zi[z],'are venit minim de',v[z])
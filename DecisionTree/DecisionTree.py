import csv
import math
import copy
d=[]
v=[]
e=[]
with open('dt.csv','r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
       e.append(dict(row))
#print(e)        

with open('dt.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        v=[]
        for i in row:
            v.append(i)
        d.append(v)
#print(d)
q=dict.fromkeys(d[0])
del q[d[0][0]]

for i in range(1,len(d[0])):
    a=input("Enter Value of attribute:")
    q[d[0][i]]=a
while(1) :    
    f=dict.fromkeys(d[0])
    g=dict.fromkeys(d[0])
    del g[d[0][0]]
    for i in range(len(d[0])):
        c1=[]
        c2=[]
        for j in range(1,len(d)):
            c1.append(d[j][i])  
        c1=list(dict.fromkeys(c1))
        f[d[0][i]]=c1

    Entropy=0
    for i in range(len(f[d[0][0]])):
        c=0
        for j in range(1,len(d)):
            if d[j][0]==f[d[0][0]][i]:
               c=c+1   
        c=c/(len(d)-1)
        Entropy = Entropy + (c*(math.log(c,2)))
    Entropy=Entropy*-1

    for i in range(1,len(d[0])):
        gain=0
        for j in range(len(f[d[0][i]])):
            l=[]
            for k in range(1,len(d)):
                if d[k][i]==f[d[0][i]][j]:
                    l.append(d[k])
            count=0
            print(l)        
            for a in range(len(f[d[0][0]])):
                c=0
                for b in range(len(l)):
                    if l[b][0]==f[d[0][0]][a]:
                         c=c+1
                print(c)
                c=c/(len(l))
                if c!=0:
                   count = count + (c*(math.log(c,2)))
                else:
                   count=count+0
            count=(count)*(len(l)/(len(d)-1))
            gain = gain + count
        gain=Entropy-(gain*-1)
        g[d[0][i]]=gain    
    print(g)  
    maximum=max(g,key=g.get)
    print(q[maximum])

    r=copy.deepcopy(d)
    d=[]
    d.append(r[0])

    p=0
    for i in range(1,len(r[0])):
        if r[0][i]==maximum:
           p=i 
           break
    print('p',p)
    
    for i in range(1,len(r)):
        print(r[i][p])
        if q[maximum]==r[i][p]:
            r[i]
            d.append(r[i])
            
    print('d',d)
    if len(d)==1:
        break
    if len(d)==2:
        print(d[1][0])
        break

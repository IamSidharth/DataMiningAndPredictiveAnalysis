import csv
import itertools

count = {};

print("Enter file name: ")

fileName=input("Enter File Name");

with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',');

    L=[None]*10;
    L[1]=set({});
    countDic={}
    for row in csv_reader:
        columnNo=0;
        for column in row:
            if(column=="1"):
                countDic[str(columnNo)] = countDic.get(str(columnNo),0)+1;
            columnNo+=1;

    for i in range(1,columnNo+1):
        if(countDic.get(str(i),0)>=2):
            L[1].add(str(i));

    #end of L1;

    print("L1: ",L[1]);

    k=2

    c=[None]*10

    while(1):

        print("--------------K:---------------",k)
        c[k] = set({})
        for x in L[k-1]:
            for y in L[k-1]:
                flag=0;
                if(x < y):
                    print('x:',x)
                    print('y:',y)
                    flag=1;
                    for i in range(0,k-2):
                        if(x[i]!=y[i]):
                            flag=0;
                            break;

                if(flag==1):
                     c[k].add(tuple(x)+tuple(y[k-2]))

                     
        if(c[k] != set({}) ):

        
            print("c ",k,": ",c[k]);
            
            L[k]=set({})
            
            for t in c[k]:
                p=[None]*k
                for j in range(0,k):
                    p[j]=int(t[j]);
                countt=0;
                with open(fileName) as csv_file:
                    csv_reader = csv.reader(csv_file,delimiter = ',');
                        
                    for row in csv_reader:
                        flag=1;
                        for i in range(k):
                            if row[p[i]]!="1":
                                flag=0;
                                break;
                        if(flag==1):    
                            countt+=1;
                    countDic[t]=countt;
                    if(countt >= 2):
                        L[k].add(t);

            print("temp L",k,": ",L[k]);

            #now pruning has to be done 
            for m in L[k]:
                for i in range(2,k+1):
                    d=tuple(itertools.combinations((m),i))
                    for s in d:
                        if(countDic.get(s,0)<2):
                            m1=set({})
                            m1.add(m)
                            L[2]=L[2]-m1;

            print("final L",k,": ",L[k]);
            k+=1;

        else:
            break;
    


        



#apriori(csv_reader,2);
#def apriori(csv_reader,minSupport):
    
        
                
        

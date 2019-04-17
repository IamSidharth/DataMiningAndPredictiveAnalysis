import csv

def dist(a,b,c,d):
    return ( (float(a)-float(b))**2 + (float(c)-float(d))**2 )**(0.5)

def kmeans(L,k):
      # c[0],c[1],c[2]

    pivot=[None]*k;
    for count in range(k):
        pivot[count]=L[count];


    first=1;
    exitt=0
    ccopy=[[] for _ in range(k)];
    while(not exitt):
        c=[[] for _ in range(k)];
        diff=[0]*k;
        for row in L:
            bigValue=99999;
            for count in range(k):
                diff[count]=dist(row[1],pivot[count][1],row[2],pivot[count][2]);
                if(diff[count]<bigValue):
                    bench=count;
                    bigValue=diff[count];        
            c[bench].append(row)


        if(first==0):
            flag=1;
            for count in range(k):
                if(c[count]!=ccopy[count]):
                    ccopy=[[] for _ in range(k)];
                    flag=0;
                    break;
                
            if(flag==1):
                for count in range(k):
                    print("-------c[",count,"]---------",c[count]);
                exitt=1;

        for count in range(k):
            sum1=0
            sum2=0
            no=0
            for ele in c[count]:
                ccopy[count].append(ele)
                sum1+=float(ele[1])
                sum2+=float(ele[2]);
                no+=1;
            pivot[count]=[0,sum1//no,sum2//no];

        if(first==1):
            first=0;

    return None;
    
    

csv_file=open('sample.csv')
csv_reader=csv.reader(csv_file,delimiter=',')
L=[];
line=0;
for row in csv_reader:
    if(line==0):
        line+=1;
    else:
        L.append(row);
kmeans(L,3)
csv_file.close();

a=int(input())
d={}
for i in range(1,a+1):
    x1=input() 
    x2=float(input()) 
    d[x1]=x2 
v=d.values()
sec=sorted(list(set(v)))
sec=sec[1]
low=[] 
for i,j in d.items():  
    if j==sec: 
        low.append(i)
    else:
    	pass
low.sort()
for i in low:
    print(i)


input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


output
Berry
Harry
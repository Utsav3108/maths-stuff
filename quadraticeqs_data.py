from pandas import *
from math import *
a=[]
b=[]
c=[]
d=[]
x1=[]
x2=[]
root=[]
index=[]


num = int(input("Enter no. readings you want to take:"))

print("....Enter Coefficients a,b,c....")

for i in range(num):
	a1= float(input("Enter a:"))
	b1=float(input("Enter b:"))
	c1=float(input("Enter c:"))
	d1 = (b1**2)-(4*a1*c1)
	print("D =",d1,"\n")
	a.append(a1)
	b.append(b1)
	c.append(c1)
	d.append(d1)
	
	if d1>0:
		print("Roots are real")
		x11=(-b1+sqrt(d1))/(2*a1)
		x22=(-b1-sqrt(d1))/(2*a1)
		
		x111=float("{:0.2f}".                    format(x11))
		
		x222=float("{:0.2f}".format(x22))
		
		x1.append(x111)
		x2.append(x222)
		print("Roots are",x111,"and",x222,"\n")
		root1=0
		root.append(root1)
		
	elif d1==0:
		print("Roots are real and equal")
		root1=-b1/2*a1
		root.append(root1)
		print("Roots:",root1,"\n")
		x11=0
		x22=0
		x1.append(x11)
		x2.append(x22)
		
	else:
		print("D is less than Zero\n")
		root1=0
		x11=0
		x22=0
		x1.append(x11)
		x2.append(x22)
		root.append(root1)
		
	index.append(i+1)
	

		
data = {
'a':a,
'b':b,
'c':c,
'd':d,
'x1':x1,
'x2':x2,
'x':root,

}
dat=DataFrame(data,index=index)
print(dat)






        
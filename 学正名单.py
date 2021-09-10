#!python3
# -*-coding : UTF-8 -*-
import sys
print(sys.version)
"""

print("helloWorld81.py is running!")

k=open("C:\\Users\\Liu Yuxuan\\Desktop\\学正中学新生名单2.txt","r")
p=k.read()
print(p)

print(" ")
l=len(p)
i=0
print("-------------P-L-E-A-S----W-A-I-T------------")
if 1:
        while i<len(p)-5:
                if(p[i]=="爸"):
                        p2=p[:i]+p[i+2:]
                        p=p2
                if(p[i]=="妈"):
                        p2=p[:i]+p[i+2:]
                        p=p2
                if(p[i]=="家"):
                        p2=p[:i-1]+p[i+3:]
                        p=p2

                i+=1


print(p)
m=open("C:\\Users\\Liu Yuxuan\\Desktop\\学正中学新生名单3.txt",'w')
m.write(p)
m.close()
print("-------------1 END^^^^^^^^^^^^------------")
"""
s=[]
m=open("C:\\Users\\Liu Yuxuan\\Desktop\\学正中学新生名单5.txt",'r')
for i in range(910):
        p=m.readline()
        if(not(p in s)):
                s.append(p);

print("----------(WRITE TO 5)---P-L-E-A-S----W-A-I-T------------")

m=open("C:\\Users\\Liu Yuxuan\\Desktop\\学正中学新生名单5.txt",'w')
for i in range(len(s)):
        if(len(s[i])==3):
                s.append(s.pop(i))

for i in range(len(s)):
        if(len(s[i])==4):
                s.append(s.pop(i))

for i in range(len(s)):
        if(len(s[i])==5):
                s.append(s.pop(i))


for i in s:
        m.write(i);
m.close()

print("-------------DONE. ^^^^^^^^^^^-------------")
while 1:
	a=1

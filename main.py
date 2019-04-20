#coding=utf-8
import urllib.request
import os
from bs4 import BeautifulSoup 
i=1000
k=1000
cnt=0
while k<=5314:
    if os.path.isfile("./luogu/"+str(k)+".html"):
        i=k-1
        while os.path.getsize("./luogu/"+str(k)+".html")==0:
            file=urllib.request.urlopen("http://www.luogu.org/problemnew/show/P"+str(k))
            data=file.read()
            fhandle=open("./luogu/"+str(i)+'.html',"wb")
            fhandle.write(data)
            fhandle.close()
            print("Fixing P"+ str(k)+"...")
    k=k+1
print("Latest Status:P" + str(i+1))
while(i<=5314):
    cnt=0
    res=urllib.request.urlopen("http://www.luogu.org/problemnew/show/P"+str(i))
    soup=BeautifulSoup(res,"html.parser")
    b=soup.find_all(text='普及/提高-')
    if len(b)>0:
        cnt=cnt+len(b)
        f=open('./TIGAOJIAN.txt','a',encoding='UTF-8',errors='ignore')
        f.write(str(i)+'\n')
        f.close
    b=soup.find_all(text='普及+/提高')
    if len(b)>0:
        cnt=cnt+len(b)
        f=open('./TIGAO.txt','a',encoding='UTF-8',errors='ignore')
        f.write(str(i)+'\n')
        f.close
    b=soup.find_all(text='提高+/省选-')
    if len(b)>0:
        cnt=cnt+len(b)
        f=open('./TIGAOJIA.txt','a',encoding='UTF-8',errors='ignore')
        f.write(str(i)+'\n')
        f.close
    
    if cnt!=0:
        file=urllib.request.urlopen("http://www.luogu.org/problemnew/show/P"+str(i))
        data=file.read()
        fhandle=open("./luogu/"+str(i)+'.html',"wb")
        fhandle.write(data)
        fhandle.close()
    i=i+1
    print("\rFinished:"+ str(round((i-1000+1)/4315*100,2))+"%  ",end=" ")

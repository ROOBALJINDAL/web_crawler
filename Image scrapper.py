from urllib import *
#m=raw_input("ENTER URL: ")
m="http://www.facebook.com/";
a=urlopen(m)
f= a.read()
f.lower();
print f

name=10101
#SEARCHING FOR LINKS WITH starting ( <a href )
x1=f.find("href")
count=f.count("<a href")
print "count of links present: ", count
f.lower();
while(count):
    m1=f[x1:].find("http")+x1
    m2=f[m1:].find('"')+m1
    print f[m1:m2]
    x1=f[m2:].find("<a href")+m2
    count-=1
    

#SEARCHING FOR IMAGES WITH starting ( <img scr= )
x1=x2=m1=m2=0
x1=f[x1:].find('<img src=')
count=f[x1:].count('<img src=')
print "count of images #case1: ", count
raw_input()
while(count):
    m1=f[x1:].find('http')+x1
    m2=f[m1:].find('"')+m1
    print f[m1:m2]
    
    url=str(name)+'.png'
    obj= open(url,'wb')
    obj.write(urlopen(f[m1:m2]).read())
    name=name+1
    #print url
    #raw_input()
    obj.close()
    
    x1=f[m2:].find('<img src=')+m2
    count-=1

#SEARCHING FOR IMAGES WITH starting ( img" src=" )
    
x1=x2=m1=m2=0
x1=f[x1:].find('img" src="')
count=f[x1:].count('img" src="')
print "count of images #case2: ", count
raw_input()

while(count):
    m1=f[x1:].find('http')+x1
    m2=f[m1:].find('"')+m1
    print f[m1:m2]
      
    url=str(name)+'.png'
    obj= open(url,'wb')
    obj.write(urlopen(f[m1:m2]).read())
    name=name+1
    print url
    #raw_input()
    obj.close()
    
    x1=f[m2:].find('img" src="')+m2
    count-=1
  

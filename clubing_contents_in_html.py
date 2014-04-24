from urllib import *
from re import *

#links=['https://www.facebook.com','http://www.techcrunch.com/','https://www.youtube.com','https://www.amazon.com','https://www.google.com/','https://www.python.org','https://www.gmail.com/','https://www.yahoo.com/','http://www.wikipedia.org']
a = urlopen('https://www.codechef.com')
html = a.read()

links= findall(r'<a href="(http.*?)"',html,I)
fileobject=open('DATAOFWEB.html','a')

for link in links:
    a = urlopen(link)
    html = a.read()
    print link,"\n"
    title= "".join(findall(r'<title.*?>[\n]?(.*?)</title>',html, M))
    content= "".join(findall(r'<meta name="description" content="(.*?)"',html))
    
    var='<a href="'+link+'"><H2>'+title+'</H2></a>'
    var=var+content+'<br>'
    var=var+'<h3 style="color: green">'+link+'</h3>'
    
    fileobject.write(var)

fileobject.close()



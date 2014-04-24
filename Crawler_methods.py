from urllib import *
from re import *
from sets import Set

#links=['https://www.facebook.com','http://www.techcrunch.com/','https://www.youtube.com','https://www.amazon.com','https://www.google.com/','https://www.python.org','https://www.gmail.com/','https://www.yahoo.com/','http://www.wikipedia.org']

global glob

def scrapeemail(website,depth):
    
    if (depth==0):
        return 0
    
    else:
        depth=depth-1
        html = urlopen(website).read()
        links= findall(r'<a href="(http.*?)"',html,I)
        fileobject=open('emails_'+str(depth)+'.csv','w')
        
        for link in links:
            html= urlopen(link).read()
            if(depth==1):
                print 'EMAILS : \n\n'
            print 'depth:',depth
            
            emails= (findall(r'[a-z_A-Z0-9.]+@[a-z_A-Z0-9.]+',html))
            
            var="\n".join(Set(emails))
            print emails,"\n\n\n"
            
            fileobject.write(var)
            scrapeemail(link,depth)
            
        fileobject.close()
    
        


    
def crawler(website,depth):
    global glob
    glob=glob+1
    if (depth==0):
        return 0
    
    else:
        depth=depth-1
        html = urlopen(website).read()
        links= findall(r'<a href="(http.*?)"',html,I)
        fileobject=open('MICROSOFT_DEPTH'+str(depth)+'.html','a')
        
        for link in links:
            html= urlopen(link).read()
            if(depth==1):
                print 'LINK IN MICROSOFT: \n\n'
            print 'depth:',depth
            print link,"\n"
            title= "".join(findall(r'<title.*?>[\n]?(.*?)</title>',html, M))
            content= "".join(findall(r'<meta name="description" content="(.*?)"',html))
            
            var='<a href="'+link+'"><H2>'+title+'</H2></a>'
            var=var+content+'<br>'
            var=var+'<h3 style="color: green">'+link+'</h3>'
            
            fileobject.write(var)
            crawler(link,depth)
        fileobject.close()
        

def doaction(website, depth, type):
    if(type == 1):
        crawler(website,depth)
    elif(type == 2):
        scrapeemail(website,depth)
       

#doaction('http://www.indschools.co.uk/direct_links_a.shtm',2,2)
glob=1
doaction('https://www.microsoft.com',3,1)



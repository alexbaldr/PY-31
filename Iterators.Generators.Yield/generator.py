from hashlib import md5


def iterator_to_md5(name):
    with open(name, "r", encoding="utf-8" ) as fi:
        links = fi.readlines()
        for i in links:            
            yield i 
            

x = iterator_to_md5("countries_links.txt")
for i in x:
    print(md5(i.encode('utf-8')).hexdigest())



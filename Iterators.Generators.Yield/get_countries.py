import json


class CountryIterator:

    def __init__(self, start, end):  
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        with open("countries.json", "r", encoding="utf-8" ) as fi:
            data = json.load(fi)
            name_counrty = data[self.start]["name"]['common']
            self.start +=1
            if self.start == self.end:
                raise StopIteration
        return name_counrty

city = CountryIterator(0, 200)
with open("countries_links.txt", "w", encoding="utf-8" ) as fo:
    for i in city:
        link = f'https://en.wikipedia.org/wiki/{i}'        
        fo.write(link + '\n')



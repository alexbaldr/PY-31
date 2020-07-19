import csv
from pymongo import MongoClient 
import pymongo
import re

client = MongoClient()
concert_bd = client['Concerts']
tickets_col = concert_bd['tickets'] 
#print(repr(tickets_col))
#print(concert_bd.list_collection_names())
#exit(0)

def read_data():
    with open ("artists.csv", 'r', encoding="utf8") as fo:    
        reader = csv.reader(fo, delimiter=",")
        art_list = list(reader)
        concerts_dict = [{"Исполнитель": id[0], 'Цена': id[1], 'Место':id[2], 'Дата':id[3]}for id in art_list[1:]]
        result = tickets_col.insert_many(concerts_dict)
        return result.inserted_ids

def find_cheapest():
    pattern = re.compile (r'\d')
    for i in tickets_col.find({'Цена': pattern}).sort("Цена", pymongo.ASCENDING):
        print (i)
        
def find_by_name(name):
    pattern = re.compile (r''+name+'+(\s|\S+)+$')
    x = [i for i in tickets_col.find({'Исполнитель': pattern}).sort("Цена", pymongo.ASCENDING)]
    print (x)


print(find_cheapest())
print(find_by_name("Th"))
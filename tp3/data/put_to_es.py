from elasticsearch import Elasticsearch
import json
import sys

es = Elasticsearch()
counter = 1

def log(c):
        sys.stdout.write(str(counter)+' documents indexed \r')
        sys.stdout.flush()

with open('data.txt') as f:
        for line in f.readlines():
                line_id = counter
                log(counter)
                counter += 1
                line = json.loads(line)
                print(line)
                es.index(index="comics", id=line_id, body=line)

print("Data loaded in Elasticsearch within tweet index")
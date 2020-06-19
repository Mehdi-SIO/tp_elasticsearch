from elasticsearch import Elasticsearch
import json
import sys

es = Elasticsearch()
c = 1


def log(c):
	sys.stdout.write(str(c)+' documents indexed \r')
	sys.stdout.flush()

with open('data.txt') as f:
	for line in f.readlines():
		line_id = c
		log(c)
		c += 1
		line = json.loads(line)
		es.index(line,  'tweets', 'tweet', line_id)
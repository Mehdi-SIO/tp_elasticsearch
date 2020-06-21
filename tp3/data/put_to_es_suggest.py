from pyes import ES
import json
import sys
from elasticsearch import Elasticsearch


conn = Elasticsearch()
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
		line['suggest'] = {
			'input': line['title'],
			'output': line['title'],
			'payload': {
				"id": line_id
			}
		}
		conn.index(body=line, index='comics', doc_type='suggest', id=line_id)

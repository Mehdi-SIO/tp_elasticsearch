from pyes import ES
import json
import sys

conn = ES()
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
		conn.index(line,  'comics', 'comic', line_id)

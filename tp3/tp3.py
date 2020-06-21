from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
import json
import os.path

app = Flask(__name__)
HERE = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/search')
def search():
	q = request.args.get('q')
	conn = Elasticsearch()
	with open('./static/query.json', 'r') as f:
		query_str = f.read()
		query = json.loads(query_str.replace('MYTEXT', q))
		res = conn.search(body=query, index="comics", doc_type="comic")
	return jsonify({
		'total': res['hits']['total'],
		'hits': res['hits']['hits']
	})


if __name__ == '__main__':
	app.run('0.0.0.0', debug=True, port=8080)

from elasticsearch import Elasticsearch

# configure elasticsearch
config = {
    'host': 'localhost'
}
es = Elasticsearch([config, ], timeout=300)

es = Elasticsearch([{'host': config.elastic_host, 'port': config.elastic_port}])


mapping = """
{
  "mappings": {
      "properties": {
          "text": {
              "type": "string"
          },
          "user": {
              "type": "string"
          },
          "created_at": {
              "type": "text"
          }
      }
  }
}
"""


es.indices.create(index="tweet", ignore=400, body=mapping)

print("Index created")
# tp_elasticsearch


* Création d'index avec mapping
```
curl -XPUT localhost:9200/tweet -H "Content-Type: application/json" -d @mapping_tweet.json
```

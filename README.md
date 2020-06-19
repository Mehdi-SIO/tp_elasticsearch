# tp_elasticsearch


* Création d'index avec mapping
```
curl -XPUT localhost:9200/tweet -H "Content-Type: application/json" -d @mapping_tweet.json
```


* Refresh sur l'index

```
curl -XPUT localhost:9200/tweet/_refresh
```
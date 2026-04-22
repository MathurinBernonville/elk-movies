# Runbook — ELK Movies Data Platform

## Prérequis
- Docker >= 24 + Docker Compose v2
- curl
- Python >= 3.10 (pour le moteur de recherche)
- Le fichier `DATA/movies.csv` téléchargé depuis Kaggle

## Lancement complet (ordre impératif)

### 1. Créer les index avec mapping
```bash
# Attendre qu'Elasticsearch soit UP d'abord :
curl http://localhost:9200/_cluster/health?pretty

# Créer movies_raw
curl -X PUT "http://localhost:9200/movies_raw" \
  -H "Content-Type: application/json" \
  -d '{"settings":{"number_of_shards":1,"number_of_replicas":0}}'

# Créer movies_clean avec mapping explicite
curl -X PUT "http://localhost:9200/movies_clean" \
  -H "Content-Type: application/json" \
  -d @elasticsearch/mappings/movies_clean_mapping.json
```

### 2. Démarrer la stack ELK
```bash
docker compose up -d
docker compose logs -f logstash   # suivre l'ingestion
```

### 3. Vérifier l'ingestion
```bash
curl http://localhost:9200/movies_raw/_count
curl http://localhost:9200/movies_clean/_count
```

### 4. Lancer le moteur de recherche
```bash
cd search_engine
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

### 5. Accéder à Kibana
```
http://localhost:5601
```

## Arrêt propre
```bash
docker compose down
```

## Reset complet (supprime les données)
```bash
docker compose down -v
```

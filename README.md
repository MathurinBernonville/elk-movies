# 🎬 ELK Movies Data Platform

Plateforme d'analyse de films construite avec la stack ELK (Elasticsearch, Logstash, Kibana).

## Stack
- Elasticsearch 8.13.0
- Kibana 8.13.0
- Logstash 8.13.0
- Python 3.10+ / Flask (moteur de recherche)

## Démarrage rapide

```bash
# 1. Placer movies.csv dans DATA/
# 2. Créer les index ES
curl -X PUT http://localhost:9200/movies_raw
curl -X PUT http://localhost:9200/movies_clean \
  -H "Content-Type: application/json" \
  -d @elasticsearch/mappings/movies_clean_mapping.json

# 3. Lancer la stack
docker compose up -d

# 4. Lancer le moteur de recherche
cd search_engine && pip install -r requirements.txt && python app.py
```

## Accès
| Service         | URL                        |
|-----------------|----------------------------|
| Elasticsearch   | http://localhost:9200      |
| Kibana          | http://localhost:5601      |
| Moteur recherche| http://localhost:5000      |

## Documentation
Voir le dossier `docs/` pour le runbook complet, le dictionnaire de données,
les règles de nettoyage et la gestion de projet.

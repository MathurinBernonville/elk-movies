# Script de démonstration

## Séquence démontrée dans demo.gif

1. **Lancement de la stack** : `docker compose up -d` — tous les services passent healthy
2. **Vérification ingestion** : `curl http://localhost:9200/movies_clean/_count` — affiche le nombre de docs
3. **Requête DSL** : exécution de R04 (films d'action en anglais post-2010) dans Kibana Dev Tools
4. **Dashboard Kibana** : navigation dans le dashboard avec les 6–8 visualisations
5. **Moteur de recherche** : recherche "space" + filtre genre "Action" → résultats paginés

## Comment reproduire
```bash
# 1. Cloner le repo
git clone <URL_DU_REPO>
cd elk-movies

# 2. Placer movies.csv dans DATA/
# 3. Créer les index
curl -X PUT http://localhost:9200/movies_raw
curl -X PUT http://localhost:9200/movies_clean -H "Content-Type: application/json" \
  -d @elasticsearch/mappings/movies_clean_mapping.json

# 4. Lancer la stack
docker compose up -d

# 5. Lancer le moteur
cd search_engine && pip install -r requirements.txt && python app.py
```

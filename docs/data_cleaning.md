# Documentation du nettoyage des données

## Anomalies observées dans movies.csv

| Anomalie                             | Champs concernés              | Fréquence estimée |
|--------------------------------------|-------------------------------|-------------------|
| Valeurs numériques à 0               | budget, revenue, runtime      | ~60% des films    |
| Champs JSON imbriqués (listes)       | genres, keywords, credits     | 100% des films    |
| Dates manquantes ou malformées       | release_date                  | ~5% des films     |
| Lignes sans titre                    | title                         | Rare              |
| Encodage UTF-8 avec caractères spec. | title, overview               | ~2% des films     |

## Règles de nettoyage appliquées (Logstash)

1. **Suppression des lignes invalides** : lignes sans `id` ou sans `title` → `drop {}`
2. **Cast de types** : tous les champs numériques castés explicitement (float/integer)
3. **Parse de date** : `release_date` converti en type `date` ES avec pattern `yyyy-MM-dd`
4. **Normalisation JSON** : `genres`, `keywords`, `production_companies` parsés avec Ruby → tableaux de strings
5. **Extraction du cast** : top 5 acteurs extraits du champ `credits` JSON
6. **Valeurs à 0 → null** : `budget`, `revenue`, `runtime` à 0 remplacés par `null` (données absentes)
7. **Suppression de champs** : `poster_path`, `backdrop_path`, `recommendations`, `credits` retirés de `movies_clean`

## Mesure d'impact avant/après nettoyage

| Métrique                         | movies_raw | movies_clean |
|----------------------------------|------------|--------------|
| Nombre de documents              | À compléter après ingestion | À compléter |
| Champs genres sous forme de liste| ❌ string JSON | ✅ keyword[] |
| budget/revenue exploitables      | ❌ 0 = ambigu | ✅ null = absent |
| release_date triable             | ❌ string    | ✅ date ES   |
| Recherche full-text optimisée    | ❌ non       | ✅ analyzer  |

> **Note** : compléter les counts après ingestion avec :
> `curl http://localhost:9200/movies_raw/_count`
> `curl http://localhost:9200/movies_clean/_count`

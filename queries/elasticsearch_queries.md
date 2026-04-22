# Requêtes Elasticsearch — Movies Clean

## R01 — Compter les documents indexés (vérification post-ingestion)
```json
GET /movies_clean/_count
```

---

## R02 — Recherche full-text sur le titre avec analyzer personnalisé
```json
GET /movies_clean/_search
{
  "query": {
    "match": {
      "title": {
        "query": "dark knight",
        "analyzer": "movie_text_analyzer"
      }
    }
  }
}
```

---

## R03 — Films les mieux notés (vote_count suffisant pour fiabilité)
```json
GET /movies_clean/_search
{
  "query": { "range": { "vote_count": { "gte": 500 } } },
  "sort":  [{ "vote_average": { "order": "desc" } }],
  "size":  10
}
```

---

## R04 — [BOOL] Films d'action en anglais sortis après 2010
```json
GET /movies_clean/_search
{
  "query": {
    "bool": {
      "must":   [
        { "term": { "genres": "Action" } },
        { "term": { "original_language": "en" } }
      ],
      "filter": [
        { "range": { "release_date": { "gte": "2010-01-01" } } }
      ]
    }
  },
  "sort": [{ "popularity": { "order": "desc" } }],
  "size": 10
}
```

---

## R05 — [BOOL] Films populaires mais peu votés (niche populaire)
```json
GET /movies_clean/_search
{
  "query": {
    "bool": {
      "must":      [{ "range": { "popularity":  { "gte": 50 } } }],
      "must_not":  [{ "range": { "vote_count":  { "gte": 1000 } } }]
    }
  },
  "size": 10
}
```

---

## R06 — [BOOL] Recherche full-text avec filtres langue + note minimale
```json
GET /movies_clean/_search
{
  "query": {
    "bool": {
      "must": [{
        "multi_match": {
          "query":  "space adventure",
          "fields": ["title^2", "overview", "tagline"]
        }
      }],
      "filter": [
        { "term":  { "original_language": "en" } },
        { "range": { "vote_average": { "gte": 7.0 } } }
      ]
    }
  }
}
```

---

## R07 — [BOOL] Flops financiers : gros budget, faible revenue
```json
GET /movies_clean/_search
{
  "query": {
    "bool": {
      "must":      [{ "range": { "budget":  { "gte": 100000000 } } }],
      "filter":    [{ "range": { "revenue": { "lte": 50000000 } } }],
      "must_not":  [{ "term":  { "status":  "In Production" } }]
    }
  },
  "sort": [{ "budget": { "order": "desc" } }],
  "size": 10
}
```

---

## R08 — [BOOL] Comédies ou romances bien notées
```json
GET /movies_clean/_search
{
  "query": {
    "bool": {
      "should": [
        { "term": { "genres": "Comedy" } },
        { "term": { "genres": "Romance" } }
      ],
      "minimum_should_match": 1,
      "filter": [
        { "range": { "vote_average": { "gte": 7.5 } } },
        { "range": { "vote_count":   { "gte": 200 } } }
      ]
    }
  }
}
```

---

## R09 — Agrégation : nombre de films par genre (Top 20)
```json
GET /movies_clean/_search
{
  "size": 0,
  "aggs": {
    "films_par_genre": {
      "terms": { "field": "genres", "size": 20 }
    }
  }
}
```

---

## R10 — Agrégation : note moyenne et nb films par langue
```json
GET /movies_clean/_search
{
  "size": 0,
  "aggs": {
    "par_langue": {
      "terms": { "field": "original_language", "size": 15 },
      "aggs": {
        "note_moyenne": { "avg":         { "field": "vote_average" } },
        "nb_films":     { "value_count": { "field": "id" } }
      }
    }
  }
}
```

---

## R11 — Histogramme : sorties par année
```json
GET /movies_clean/_search
{
  "size": 0,
  "aggs": {
    "sorties_par_annee": {
      "date_histogram": {
        "field":             "release_date",
        "calendar_interval": "year",
        "format":            "yyyy"
      }
    }
  }
}
```

---

## R12 — Top films par ROI (revenue / budget) via script Painless
```json
GET /movies_clean/_search
{
  "query": {
    "bool": {
      "filter": [
        { "range": { "budget":  { "gt": 1000000 } } },
        { "range": { "revenue": { "gt": 0 } } }
      ]
    }
  },
  "sort": [{
    "_script": {
      "type":   "number",
      "script": { "source": "doc['revenue'].value / doc['budget'].value" },
      "order":  "desc"
    }
  }],
  "size": 10,
  "_source": ["title", "budget", "revenue", "release_date"]
}
```

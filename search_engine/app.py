from flask import Flask, request, render_template, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es  = Elasticsearch("http://localhost:9200")
IDX = "movies_clean"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    q        = request.args.get("q", "")
    genre    = request.args.get("genre", "")
    language = request.args.get("language", "")
    year     = request.args.get("year", "")
    page     = int(request.args.get("page", 1))
    size     = 10
    from_    = (page - 1) * size

    must_clauses   = []
    filter_clauses = []

    if q:
        must_clauses.append({
            "multi_match": {
                "query":     q,
                "fields":    ["title^3", "overview", "tagline"],
                "type":      "best_fields",
                "fuzziness": "AUTO"
            }
        })
    else:
        must_clauses.append({"match_all": {}})

    if genre:
        filter_clauses.append({"term": {"genres": genre}})
    if language:
        filter_clauses.append({"term": {"original_language": language}})
    if year:
        filter_clauses.append({
            "range": {
                "release_date": {
                    "gte": f"{year}-01-01",
                    "lte": f"{year}-12-31"
                }
            }
        })

    body = {
        "from":  from_,
        "size":  size,
        "query": {
            "bool": {
                "must":   must_clauses,
                "filter": filter_clauses
            }
        },
        "_source": [
            "title", "overview", "genres", "original_language",
            "release_date", "vote_average", "vote_count", "popularity"
        ]
    }

    resp    = es.search(index=IDX, body=body)
    hits    = resp["hits"]["hits"]
    total   = resp["hits"]["total"]["value"]
    results = [{
        "title":    h["_source"].get("title", "N/A"),
        "overview": (h["_source"].get("overview", "") or "")[:200],
        "genres":   h["_source"].get("genres", []),
        "language": h["_source"].get("original_language", ""),
        "date":     str(h["_source"].get("release_date", ""))[:10],
        "score":    round(h.get("_score") or 0, 2),
        "rating":   h["_source"].get("vote_average", 0),
    } for h in hits]

    return jsonify({"total": total, "results": results, "page": page})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

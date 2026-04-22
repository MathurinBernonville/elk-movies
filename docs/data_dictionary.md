# Dictionnaire de données — movies_clean

| Champ                 | Type ES   | Type source | Description                                      | Nettoyage appliqué                       |
|-----------------------|-----------|-------------|--------------------------------------------------|------------------------------------------|
| id                    | integer   | string      | Identifiant unique du film                       | Cast en integer                          |
| title                 | text      | string      | Titre du film                                    | Indexé avec movie_text_analyzer          |
| overview              | text      | string      | Synopsis                                         | Indexé avec movie_text_analyzer          |
| tagline               | text      | string      | Slogan du film                                   | Indexé avec movie_text_analyzer          |
| original_language     | keyword   | string      | Langue originale (code ISO)                      | Aucun                                    |
| status                | keyword   | string      | Statut (Released, In Production…)                | Aucun                                    |
| genres                | keyword[] | JSON string | Liste des genres                                 | Parsing JSON → tableau de noms           |
| keywords              | keyword[] | JSON string | Mots-clés associés                               | Parsing JSON → tableau de noms           |
| production_companies  | keyword[] | JSON string | Sociétés de production                           | Parsing JSON → tableau de noms           |
| cast                  | keyword[] | JSON string | Top 5 acteurs (extrait de credits)               | Parsing JSON → 5 premiers noms           |
| release_date          | date      | string      | Date de sortie                                   | Parse date yyyy-MM-dd                    |
| popularity            | float     | string      | Score de popularité TMDB                         | Cast en float                            |
| vote_average          | float     | string      | Note moyenne (0–10)                              | Cast en float                            |
| vote_count            | integer   | string      | Nombre de votes                                  | Cast en integer                          |
| budget                | long      | string      | Budget en USD                                    | Cast en integer, 0 → null               |
| revenue               | long      | string      | Revenus en USD                                   | Cast en integer, 0 → null               |
| runtime               | integer   | string      | Durée en minutes                                 | Cast en integer, 0 → null               |

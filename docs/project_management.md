# Gestion de projet

## Contexte
Projet réalisé individuellement. Le Gitflow et les PR sont maintenus
pour assurer la traçabilité et démontrer une démarche professionnelle.

## Gitflow appliqué

| Branche                    | Rôle                        |
|----------------------------|-----------------------------|
| `main`                     | Version stable, livraison   |
| `dev`                      | Intégration continue        |
| `feature/bootstrap-stack`  | Docker Compose ELK          |
| `feature/ingestion-raw`    | Pipeline movies_raw         |
| `feature/cleaning-mapping` | Pipeline movies_clean       |
| `feature/queries`          | 12 requêtes DSL             |
| `feature/kibana-dashboard` | Visualisations Kibana       |
| `feature/search-engine`    | Moteur de recherche Flask   |
| `feature/documentation`    | Docs complètes              |

## Ordre de merge
1. feature/bootstrap-stack → dev
2. feature/ingestion-raw → dev
3. feature/cleaning-mapping → dev
4. feature/queries → dev
5. feature/kibana-dashboard → dev
6. feature/search-engine → dev
7. feature/documentation → dev
8. dev → main (livraison finale)

## Pull Requests en solo
Chaque PR est ouverte sur GitHub avec description, changements, et auto-review.
Aucun push direct sur `main` ou `dev`.

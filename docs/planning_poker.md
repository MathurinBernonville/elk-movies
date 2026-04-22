# Planning Poker

## 1) Participants
> Projet réalisé en solo. Les estimations ont été produites en simulant
> plusieurs perspectives (développeur, data engineer, utilisateur final)
> afin de respecter l'esprit de la méthode.

- Membre unique : [TON PRÉNOM] — Lead technique, data engineer, rédacteur

## 2) Échelle utilisée
Fibonacci : 1, 2, 3, 5, 8, 13

## 3) Stories estimées

| ID    | User Story                          | Votes simulés | Estimation finale | Hypothèses                             | Owner |
|-------|-------------------------------------|---------------|-------------------|----------------------------------------|-------|
| US-01 | Bootstrap Docker Compose ELK        | 2, 2, 3, 2    | 2                 | Docker déjà installé sur la machine    | Solo  |
| US-02 | Ingestion brute movies_raw          | 3, 3, 5, 3    | 3                 | Format CSV stable, pas de BOM          | Solo  |
| US-03 | Nettoyage + indexation movies_clean | 5, 5, 8, 5    | 5                 | Champs JSON imbriqués à parser en Ruby | Solo  |
| US-04 | Mapping + analyzer personnalisé     | 3, 3, 3, 5    | 3                 | Schéma figé avant création de l'index  | Solo  |
| US-05 | 12 requêtes DSL commentées          | 3, 3, 5, 3    | 3                 | Index movies_clean peuplé et stable    | Solo  |
| US-06 | Dashboard Kibana (6–8 visu)         | 3, 5, 5, 3    | 5                 | Data View créé, données propres        | Solo  |
| US-07 | Moteur de recherche Flask           | 5, 5, 8, 5    | 5                 | Flask + elasticsearch-py disponibles   | Solo  |
| US-08 | Documentation complète              | 3, 3, 3, 5    | 3                 | Rédigée en parallèle des features      | Solo  |

**Total estimé : 29 points**

## 4) Décisions de découpage

- **Story** : US-03 estimée à 8 par une perspective
- **Découpage** : séparée en deux sous-tâches (parsing JSON des listes / conversions de types)
- **Risque** : format des champs `genres`, `keywords`, `credits` potentiellement inconsistant
- **Action** : tester le pipeline sur un échantillon avant ingestion complète

## 5) Répartition finale des features

- **Solo** : F1 Bootstrap · F2 Ingestion brute · F3 Nettoyage · F4 Mapping
             F5 Requêtes · F6 Kibana · F7 Documentation · F8 Moteur de recherche

# Music Data ETL Processor

Project by Jackson Le, Joanne Lee, Kenny Nguyen.

---

## Project Overview

This project processes, cleans, enriches, and merges Grammy nominees/winners, Billboard Hot 100 songs, and Spotify metadata to analyze songs with both commercial and critical success.

---

## Important Files

- `Cleaning.py`: Cleans both Kaggle datasets.
- `Hot100andGrammysMerging.py`: Merges both Kaggle datasets.
- `Main.py`: Enriches dataset, allows modifications.
- `API.py`: Handles Spotify API calls & column functions.
- `project_dss.ipynb`: Contains SQLite database setup & data analysis & visualizations.
- `hot100_grammys_merged.csv`: Cleaned and merged dataset containing the two from Kaggle.
- `api_kaggle_final.csv`: Final dataset containing all three sources.

---

## How to Use

1. **Data Wrangling:**  
   Run `Cleaning.py` to clean both the Grammy & Hot100 datasets. Then run `Hot100andGrammysMerging.py`, this will output `hot100_grammys_merged.csv`.

2. **Enrichment:**  
   Run `main.py` to enrich the merged dataset with Spotify API song data, apply any column modifications, and handle CSV/JSON conversions. The final output is `api_kaggle_final.csv`.

3. **Database Insertion & Analysis:**  
   Open `project_dss.ipynb` to load the cleaned datasets into an SQLite database and perform further analysis and visualization.

---



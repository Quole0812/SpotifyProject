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

## ETL Processor (main.py) Explanation

The `main.py` file serves as the core of the ETL processor. Here's how to use it:

1. **Spotify API Integration:**  
   Running `main.py` will fetch audio features from Spotify based on the songs in `hot100_grammys_merged.csv`.

2. **Data Modification:**  
   You can also modify the dataset by adding new columns and values, updating existing values or deleting columns.

3. **Format Conversion:**  
   You can also convert the dataset between CSV and JSON, depending on your desired format.

4. **Final Output:**  
   The final dataset is then saved as `Api_kaggle_final.csv`, ready for analysis or to be inserted into a database.

--- 

## Jupyter Notebook Explanation


---

## Conclusions from Data Visualization and Analysis

🚀 SpaceX Launch ETL Pipeline

A Python-based ETL project using the SpaceX public API

This project demonstrates a full ETL workflow (Extract → Transform → Load) using Python and the SpaceX v4 public API. The goal is to extract rocket launch data, transform nested JSON into a clean DataFrame, and analyze success vs. failure rates across all historical launches.

📡 1. Extract

We retrieve launch data from:

https://api.spacexdata.com/v4/launches


This endpoint returns detailed records for every SpaceX launch, including:

success/failure

rocket ID

mission name

date/time

links

details

import requests
import pandas as pd

API_URL = "https://api.spacexdata.com/v4/launches"
data2 = requests.get(API_URL).json()

🧩 2. Transform — Flatten + Filter

SpaceX returns nested JSON, so we use pd.json_normalize() to flatten it:

df = pd.json_normalize(data2)


Then we separate successful and unsuccessful launches:

df_success = df[df["success"] == True]
df_failures = df[df["success"] == False]

print(f"Successful launches: {len(df_success)}.")
print(f"Unsuccessful launches: {len(df_failures)}.")

✔ Example Transformations

Flattening nested JSON structures

Creating success/failure subsets

Displaying sample rows with .head()

📊 3. Analysis (Exploratory)

With the data flattened, we can easily explore:

Launch success trends

Launch failures

Rocket performance

Time-series trends (by year, rocket, payload, etc.)

Example:

df["year"] = pd.to_datetime(df["date_utc"]).dt.year
df.groupby("year")["success"].mean()

🗄 4. (Optional) Load Into SQL

Setup using SQLAlchemy:

from sqlalchemy import create_engine

engine = create_engine("postgresql://username:password@localhost:5432/spacex")

df_success.to_sql("spacex_success", engine, if_exists="replace", index=False)
df_failures.to_sql("spacex_failures", engine, if_exists="replace", index=False)

📁 Project Structure
spacex-launch-etl-pipeline/
│
├── extract.py
├── transform.py
├── load.py        (optional)
├── spacex_etl.ipynb
├── README.md
└── requirements.txt

🧠 Skills Demonstrated

Python ETL pipeline design

Working with REST APIs

Nested JSON normalization

pandas filtering & transformation

Data exploration & analysis

SQL loading (optional)

Clear function-based pipeline structure

🚀 Future Enhancements

Merge rocket metadata (rocket names, height, mass)

Visualize success rate trends

Power BI or matplotlib launch dashboards

Build a scheduler (cron / Windows Task Scheduler)

Create a machine learning prediction model for launch success

📄 License

Open for educational and portfolio use.

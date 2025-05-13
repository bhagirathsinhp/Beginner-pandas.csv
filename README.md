# 🐿️ Central Park Squirrel Fur Color Counter

This project analyzes the 2018 Central Park Squirrel Census dataset and counts the number of squirrels by their primary fur color. It reads the dataset, filters it based on fur color, and outputs a summary as a new CSV file.

---
## 📂 Project Files

- **main.py** — The core script that:

  - Reads squirrel data from a `.csv` file
  - Counts squirrels with Gray, Black, and Cinnamon fur
  - Creates a summary DataFrame
  - Outputs the result to `new_data.csv`

- **2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250430.csv** — The dataset used for analysis
- **new_data.csv** — The generated summary CSV file containing the fur color counts

---
## 🧪 How It Works

### 1. Load the dataset
The script uses `pandas` to read the squirrel dataset:

    data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250430.csv')

### 2. Count Fur Colors
It defines a function count_fur_total(color) that filters the Primary Fur Color column and counts entries for:
- Gray
- Black
- Cinnamon

### 3. Create summary
The script creates a dictionary and converts it into a new DataFrame:

    data_dict = {
        "Fur Color": ["Gray", "Black", "Cinnamon"],
        "Count": [gray_fur, black_fur, cinnamon_fur],
    }

### 4. Save results
The summary is written to new_data.csv:

    data_csv.to_csv("new_data.csv")

---
## 📦 Requirements

    Python 3.x

    pandas

Install dependencies with:

    pip install pandas

---
## 🚀 How to Run

    python main.py

After running, a new_data.csv file will be created in the same directory with the squirrel fur color counts.

---
## 👤 Author

[![GitHub: bhagirathsinhp](https://img.shields.io/github/followers/bhagirathsinhp?label=Follow&style=social)](https://github.com/bhagirathsinhp)
[![LinkedIn: Bhagirath Parmar](https://img.shields.io/badge/-Bhagirath%20Parmar-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/bhagirath-parmar-385865269/)](https://www.linkedin.com/in/bhagirath-parmar-385865269/)

# Last-Mile Delivery Performance Analysis

> **Python (Pandas, NumPy) · Jupyter Notebook · Tableau Public**

## Business Problem

This project analyzes food-delivery orders to understand how much time is spent preparing an order and transporting it to the customer. The cleaned data also includes time-of-day categories and a flag based on the third quartile of total delivery time, which can support further analysis of delivery patterns.

---

## Key Insights

The analysis is still in progress. Add 2–3 findings here after analyzing the cleaned dataset or building the Tableau dashboard. Use measured values from the project rather than example numbers.

- **Finding 1:** Add a result about preparation time versus transit time.
- **Finding 2:** Add a result about delivery times across time-of-day categories.
- **Finding 3:** Add another supported result, such as differences by city or vehicle type.

---


## Repository Structure

```text
├── data/
│   └── train.csv              # Raw dataset downloaded from Kaggle
├── FoodDelivery.ipynb         # Data cleaning, calculations, and feature engineering
└── README.md
```

## Dataset

- **Source:** [Food Delivery Dataset on Kaggle](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset?select=train.csv)
- **File:** `train.csv`
- **Data includes:** delivery-partner details, order and pickup times, weather and road conditions, vehicle information, city type, festival status, and total delivery duration.

---

## Data Preparation Workflow

All processing steps are implemented in [`FoodDelivery.ipynb`](FoodDelivery.ipynb).

| Step | Stage | What the code does |
|---:|---|---|
| 1 | Import libraries | Imports Pandas, NumPy, and `time` from `datetime`. |
| 2 | Load dataset | Reads `data/train.csv` into a Pandas DataFrame named `data`. |
| 3 | Trim whitespace | Removes leading and trailing spaces from values in text columns. |
| 4 | Remove invalid placeholders | Defines a list of invalid text values and removes every row containing one of those values in any column. |
| 5 | Prepare delivery-time column | Removes the `"(min) "` text from `Time_taken(min)`, converts the remaining value to an integer, and sorts the data by delivery time. |
| 6 | Calculate IQR fences | The `IQR(data, column)` function uses the sorted column to identify the first- and third-quarter positions, calculates the IQR, and returns the upper fence, lower fence, and third-quarter value. |
| 7 | Filter delivery-time outliers | Keeps rows where `Time_taken(min)` is between the calculated lower and upper fences. |
| 8 | Calculate preparation time | Converts `Time_Orderd` and `Time_Order_picked` from `HH:MM` to minutes, then subtracts order time from pickup time. Rows with preparation time less than or equal to zero are removed. |
| 9 | Calculate transit time | Subtracts preparation time from `Time_taken(min)`. Rows with transit time less than or equal to zero are removed. |
| 10 | Calculate total delivery time | Adds preparation time and transit time to create `Total_delivery_time(min)`, then sorts the DataFrame by this column. |
| 11 | Categorize order time | Creates `Time_Category` based on the hour in `Time_Orderd`: Breakfast, Lunch Peak, Afternoon, Dinner Rush, or Late Night. |
| 12 | Create the flag | Calls the IQR function for `Total_delivery_time(min)` and creates `Flag`, set to `True` when total delivery time is less than or equal to the third-quarter value, and `False` otherwise. |

### IQR Function

The notebook's `IQR(data, column)` function returns three values:

- `upperfence`: the upper outlier boundary.
- `lowerfence`: the lower outlier boundary.
- `third`: the third-quarter value used as the threshold for the `Flag` column.

The notebook uses the fences to filter outliers from `Time_taken(min)`. It then uses the third-quarter value of `Total_delivery_time(min)` to create the `Flag` column.

### Engineered Features

| Column | Meaning |
|---|---|
| `Time_prep(min)` | Minutes between the order being placed and picked up. |
| `Transit_time(min)` | Estimated minutes spent in transit, calculated as total recorded time minus preparation time. |
| `Total_delivery_time(min)` | Sum of preparation time and transit time. |
| `Time_Category` | Category based on the hour the order was placed. |
| `Flag` | `True` when `Total_delivery_time(min)` is less than or equal to the third-quarter threshold; otherwise `False`. |

### Time-of-Day Categories

| Hour | Category |
|---|---|
| 06:00–10:59 | Breakfast |
| 11:00–14:59 | Lunch Peak |
| 15:00–17:59 | Afternoon |
| 18:00–21:59 | Dinner Rush |
| 22:00–05:59 | Late Night |

### Remaining Tasks

- [ ] Export the cleaned dataset to `data/clean_delivery_data.csv` for Tableau.
- [ ] Build and publish the Tableau Public dashboard.
- [ ] Add the real dashboard URL and screenshot above.
- [ ] Replace the placeholder key insights with findings from the completed analysis.

---


## Tech Stack

- **Python** — data processing and calculations
- **Pandas** — data cleaning and DataFrame operations
- **NumPy** — numerical computing library imported in the notebook
- **Jupyter Notebook** — analysis workflow

---


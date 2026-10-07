# 📦 Last-Mile Delivery Performance Analysis

> **Python (Pandas, NumPy) · Jupyter · Tableau Public**

## Business Problem

Delivery times on an on-demand food delivery platform have surged over the past quarter, driving up customer complaints. This project cleans the raw order data and breaks each delivery into **kitchen prep time** and **transit time** to find out whether the bottleneck is restaurant prep, traffic/transit, or peak hours.

---

## 🔍 Key Insights

<!-- TODO: replace with your real findings once the analysis/dashboard is done. Keep it to 2–3 bullets with numbers. -->

1. **[Insight 1]** – e.g. "Transit time accounts for X% of total delivery time, while prep time accounts for Y%."
2. **[Insight 2]** – e.g. "Delays peak during the dinner rush (HH:MM–HH:MM), with X% of orders delayed vs. Y% off-peak."
3. **[Insight 3]** – e.g. "Vehicle type / city X has the longest average delivery time (N min)."

---

## 📊 Interactive Dashboard

**🔗 Live dashboard:** [View on Tableau Public](https://public.tableau.com/) <!-- TODO: paste your dashboard link -->

![Dashboard Screenshot](images/dashboard.png) <!-- TODO: add screenshot to /images -->

The dashboard covers delay hotspots, peak-hour bottlenecks, and vehicle performance.

---

## 📁 Repository Structure

```
├── data/
│   └── train.csv              # Raw dataset (download from Kaggle, see below)
├── FoodDelivery.ipynb         # Data cleaning & feature engineering notebook
├── images/
│   └── dashboard.png          # Dashboard screenshot
└── README.md
```

## 🗂 Dataset

- **Source:** [Food Delivery Dataset on Kaggle](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset?select=train.csv) (`train.csv`)
- **Raw size:** 45,593 orders
- **Contents:** delivery partner ID, age and ratings; restaurant and delivery coordinates; order date; order and pickup times; weather and road traffic conditions; order type; vehicle type and condition; city type; festival flag; and total time taken (min).

---

## 🧹 Data Preparation Pipeline

All steps live in [`FoodDelivery.ipynb`](FoodDelivery.ipynb).

| # | Step | What it does |
|---|------|--------------|
| 1 | **Load** | Reads `data/train.csv` with Pandas. |
| 2 | **Trim whitespace** | Strips leading/trailing spaces from every text column. |
| 3 | **Remove invalid values** | Drops any row containing placeholder strings such as `NaN`, `None`, `null`, `NA`, `N/A`, `False`, `Unknown` (case variants included). **45,593 → 41,368 rows.** |
| 4 | **Parse target** | Converts `Time_taken(min)` from text (e.g. `"(min) 24"`) to an integer. |
| 5 | **Outlier removal (IQR)** | Computes Q1 = 19 min and Q3 = 33 min (IQR = 14), then keeps only orders within the 1.5×IQR fences (upper fence = **54 min**). |
| 6 | **Prep time** | `Time_Order_picked − Time_Orderd` in minutes. Rows with prep time ≤ 0 are dropped. |
| 7 | **Transit time** | `Time_taken(min) − Time_prep(min)`. Rows with transit time ≤ 0 are dropped. |
| 8 | **Total delivery time** | `Time_prep(min) + Transit_time(min)`. |

### Engineered features

| Column | Description |
|--------|-------------|
| `Time_prep(min)` | Minutes from order placed to order picked up (kitchen prep). |
| `Transit_time(min)` | Minutes from pickup to delivery (travel). |
| `Total_delivery_time(min)` | Prep + transit. |

### 🚧 Roadmap

- [ ] Time-of-day categories (e.g. Breakfast, Lunch Peak, Afternoon, Dinner Rush, Late Night)
- [ ] Delayed-order flag (e.g. total delivery time above a defined threshold)
- [ ] Export the clean dataset to `data/clean_delivery_data.csv` for Tableau
- [ ] Publish the Tableau Public dashboard and fill in the links above

<!-- Delete the roadmap items as you complete them. -->

---

## ⚙️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Install dependencies
pip install pandas numpy jupyter

# 3. Download train.csv from Kaggle and place it in the data/ folder

# 4. Launch the notebook
jupyter notebook FoodDelivery.ipynb
```

## 🛠 Tech Stack

- **Python 3** – Pandas, NumPy
- **Jupyter Notebook** – analysis and documentation
- **Tableau Public** – interactive dashboard

---

## 👤 Author

**[Your Name]** · [LinkedIn](https://www.linkedin.com/) · [GitHub](https://github.com/)

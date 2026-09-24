# 🌿 CropSense — Seasonal Farm Analytics

A full-stack data analysis web application built with **Python + Flask** that analyses 4,000 Indian farm records across crops, seasons, states, and irrigation methods to surface actionable agricultural insights.

---

## 📁 Project Structure

```
cropsense/
├── app.py                  # Flask REST API & frontend routes
├── analysis.py             # Core data analysis engine (Pandas + NumPy)
├── requirements.txt        # Python dependencies
├── data/
│   └── seasonal_agriculture_performance_dataset.csv
├── templates/
│   ├── base.html           # Shared layout (navbar, footer)
│   ├── index.html          # Home page with KPIs and insights
│   ├── dashboard.html      # Interactive analytics dashboard (5 tabs)
│   ├── explorer.html       # Filterable, paginated data table
│   └── report.html         # Printable analysis report
└── static/
    ├── css/style.css       # Full responsive stylesheet
    └── js/
        ├── main.js         # Shared fetch + utility functions
        ├── index.js        # Home page logic
        ├── dashboard.js    # All dashboard charts (Chart.js)
        ├── explorer.js     # Data explorer with filters + pagination
        └── report.js       # Auto-generated report builder
```

---

## 🗂️ Dataset

**File:** `seasonal_agriculture_performance_dataset.csv`  
**Records:** 4,000 farm entries  
**Columns (27):**

| Column | Description |
|---|---|
| Farm_ID | Unique farm identifier |
| State / District | Geographic location |
| Crop | Crop type (Wheat, Rice, Maize, Cotton, Chilli, Sugarcane, Groundnut, Pulses) |
| Season | Growing season (Kharif, Rabi, Zaid) |
| Farm_Area_Hectares | Farm size in hectares |
| Rainfall_mm | Seasonal rainfall received |
| Avg_Temperature_C | Average temperature (°C) |
| Humidity_pct | Relative humidity (%) |
| Sunlight_Hours_Day | Daily sunlight hours |
| Soil_pH / Soil_Moisture_pct | Soil quality indicators |
| Nitrogen/Phosphorus/Potassium_kg_ha | Nutrient application rates |
| Irrigation_Method | Drip / Flood / Sprinkler / Rainfed |
| Fertilizer_kg_ha / Pesticide_Litre_ha | Input quantities |
| Seed_Quality_Score | Seed quality (0–1 scale) |
| Yield_Tonnes_Ha | Crop yield in t/ha (target variable) |
| Production_Tonnes | Total production |
| Market_Price_INR_Tonne | Market price in INR per tonne |
| Total_Cost_INR / Revenue_INR / Profit_INR | Financial metrics |
| Water_Used_m3 / Water_Efficiency_t_per_1000m3 | Water metrics |
| Disease_Pest_Risk_pct | Disease & pest risk percentage |

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
cd agri_analysis
pip install -r requirements.txt
```

### 2. Run the application
```bash
python app.py
```

### 3. Open your browser
```
http://localhost:5000
```

---

## 🌐 Pages

| URL | Description |
|---|---|
| `/` | Home — KPI cards, key insights, API reference |
| `/dashboard` | Analytics dashboard — 5 tabbed views with Chart.js charts |
| `/explorer` | Data explorer — filterable & paginated table (by crop/season/state) |
| `/report` | Printable analysis report with tables, insights & recommendations |

---

## 🔌 REST API Endpoints

All endpoints return JSON in the format:
```json
{ "status": "ok", "data": <payload> }
```

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/summary` | Dataset overview & descriptive statistics |
| GET | `/api/v1/yield/by-crop` | Yield stats grouped by crop |
| GET | `/api/v1/yield/by-season` | Yield stats grouped by season |
| GET | `/api/v1/yield/by-state` | Yield stats grouped by state |
| GET | `/api/v1/profitability` | Profitability metrics by crop |
| GET | `/api/v1/irrigation` | Yield & water efficiency by irrigation method |
| GET | `/api/v1/correlation` | Pearson correlation matrix for key features |
| GET | `/api/v1/heatmap/season-crop` | Season × Crop average yield pivot |
| GET | `/api/v1/farms/top-bottom?n=10` | Top & bottom N farms by yield |
| GET | `/api/v1/rainfall-yield` | Average yield per rainfall bucket |
| GET | `/api/v1/disease-risk` | Disease & pest risk statistics by crop |
| GET | `/api/v1/water-efficiency` | Water efficiency by state |
| GET | `/api/v1/seed-quality` | Seed quality vs yield scatter sample |
| GET | `/api/v1/insights` | Auto-generated key insights |
| GET | `/api/v1/records?page=1&page_size=50&crop=&season=&state=` | Paginated raw records |

---

## 📊 Dashboard Tabs

1. **Yield Analysis** — Yield by crop (bar), by season (doughnut), by state (horizontal bar), Season × Crop heatmap
2. **Profitability** — Profit by crop, profit margin %, top/bottom 10 farm tables
3. **Water & Irrigation** — Yield by irrigation method, water efficiency comparison, state-level efficiency
4. **Climate Impact** — Yield by rainfall bucket, seed quality vs yield scatter, correlation heatmap
5. **Disease Risk** — Average and max disease/pest risk by crop

---

## 🔍 Key Insights (from analysis)

- **Sugarcane** leads in yield per hectare due to its high production characteristics
- **Chilli** generates the highest average profit per farm record
- **Drip irrigation** outperforms other methods in water efficiency
- Farms receiving **400–600 mm** rainfall tend to achieve optimal yields
- **Disease/pest risk is highest** for Cotton and Pulses under humid Kharif conditions
- **Seed quality** shows a positive correlation with yield across all crop types

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.10+, Flask 3.0, Flask-CORS |
| Data Analysis | Pandas 2.2, NumPy 1.26, SciPy 1.13 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Charts | Chart.js 4.4 (CDN) |
| Deployment | Gunicorn (production WSGI server) |

---

## 📋 Requirements

See [`requirements.txt`](requirements.txt):
```
flask==3.0.3
flask-cors==4.0.1
pandas==2.2.2
numpy==1.26.4
scipy==1.13.1
matplotlib==3.9.0
seaborn==0.13.2
scikit-learn==1.5.0
openpyxl==3.1.4
gunicorn==22.0.0
```

---

## 🏃 Production Deployment

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## 👨‍💻 Author

**G Karthikeya**

Built with Python / Flask · Seasonal Agriculture Performance Dataset

> 🌿 CropSense — Seasonal Farm Analytics | [GitHub](https://github.com/luffv)

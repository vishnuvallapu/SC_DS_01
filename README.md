# Demographic Data Visualization

This project contains a clean, production-grade demographic analysis pipeline. The task is to visualize the distribution of demographic data (e.g. populations, country regions).

Here, we utilize the official **World Bank Total Population and Country Metadata** dataset to plot country-level populations (continuous comparison) and geographic distributions (categorical distribution).

---

## 📁 Repository Structure

```text
├── data/
│   ├── population.csv         # Raw population total data (1960 - 2023)
│   └── metadata.csv           # Country geographic and income metadata
├── download_data.py           # Self-contained script to download and structure the dataset
├── population_visualization.ipynb # Clean Jupyter Notebook for static visualization
├── requirements.txt           # Python library dependencies
└── README.md                  # Project guide and explanation (this file)
```

---

## 🚀 Getting Started (Step-by-Step Setup)

Follow these simple steps to run and explore this project on your local machine:

### 1. Set Up Your Python Environment
Install the required libraries:
```bash
pip install -r requirements.txt
```

### 2. Download the Dataset
Run the automated download script that fetches the dataset from the World Bank API, extracts it, and structures it into the `data/` folder:
```bash
python download_data.py
```

### 3. Run the Jupyter Notebook
Open the notebook in your IDE or run:
```bash
jupyter notebook population_visualization.ipynb
```
Follow the cells to see:
* How the data is loaded and merged.
* Specific Country Name vs Population plotted as coordinates (X: Country Name, Y: Population).
* Geographic Region distribution bar chart.


## 📊 Key Visualization Details

* **Country Name vs Population (Graph Coordinates)**: Compares specific country sizes directly. The X-coordinate represents the Country Name, and the Y-coordinate represents the Population (in Millions).
* **Countries by Region (Categorical Distribution)**: Uses a horizontal bar chart to count how many countries reside in each geographic region.

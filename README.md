## 📌 Overview

**AI Self-Healing Cities** is a machine learning prototype built using **Google Colab** that classifies Air Quality Index (AQI) categories and simulates pollution-reduction interventions to measure their impact.

Unlike traditional AQI dashboards that only display current pollution levels, this system enables:

* Predictive AQI categorization
* Geospatial pollution pattern analysis
* What-if intervention simulation
* Data-driven environmental policy evaluation

It transforms pollution monitoring into an **AI-powered decision-support tool**.

---

## 🎯 Problem Statement

Urban regions face critical air pollution challenges. Policymakers need tools that:

* Predict AQI categories
* Simulate pollution control strategies
* Quantify expected improvements
* Support evidence-based governance

Most systems provide only real-time monitoring.
This project introduces predictive modeling and intervention analysis.

---

## 🛠 Built Using

* **Google Colab** (Development Environment)
* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

---

## 🧠 Technical Approach

### 1️⃣ Data Processing

* Delhi AQI dataset (CSV format)
* Removed missing values from `pollutant_avg`
* Selected features:

  * `latitude`
  * `longitude`
  * `pollutant_min`
  * `pollutant_max`

---

### 2️⃣ AQI Categorization

| AQI Range | Category |
| --------- | -------- |
| 0–50      | Good     |
| 51–100    | Moderate |
| 101–200   | Poor     |
| >200      | Severe   |

---

### 3️⃣ Machine Learning Model

**Model Used:** RandomForestClassifier (Scikit-Learn)

Why Random Forest?

* Handles non-linear pollution relationships
* Robust to noisy environmental data
* Provides feature importance insights
* Strong baseline classification model

---

### 4️⃣ Model Evaluation

* Accuracy Score
* Weighted F1 Score
* Confusion Matrix
* Feature Importance Graph

---

## 🔥 Core Innovation: What-If Intervention Simulation

The system simulates environmental intervention scenarios.

### Example:

* Reduce `pollutant_max` by 20%
* Re-run predictions
* Compare AQI category distribution before vs after intervention

### This Enables:

* Emission reduction policy testing
* Traffic control strategy simulation
* Industrial regulation impact analysis
* Environmental planning support

Instead of asking:

> "What is today's AQI?"

The system answers:

> "What happens if pollution is reduced by 20%?"

---

## 📊 Outputs Generated

* Confusion Matrix
* Feature Importance Visualization
* Prediction Samples
* AQI Distribution Comparison
* Before vs After Intervention Graph

---

## 📂 Project Structure

```
AI-Self-Healing-Cities/
│
├── Delhi_AQI_Prototype.ipynb
├── Delhi_AQI_2026.csv
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run (Google Colab)

1. Open Google Colab
2. Upload `Delhi_AQI_Prototype.ipynb`
3. Upload dataset CSV
4. Run all cells

No local setup required.

---

## 🌍 Vision

AI Self-Healing Cities demonstrates how AI can:

* Move beyond pollution monitoring
* Enable predictive environmental governance
* Support sustainable urban planning
* Provide data-driven policy insights

This prototype lays the foundation for scalable environmental AI systems.

---

## 👨‍💻 Author

**Vivek Kumar**
GitHub: [https://github.com/Vivekkumar161122](https://github.com/Vivekkumar161122)

---

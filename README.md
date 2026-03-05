# 🎯 Intern Performance Prediction

A machine learning project to predict intern performance scores
using Random Forest and XGBoost regression models.

---

## 📋 Project Overview
| Item | Detail |
|------|--------|
| Dataset | 10,000 synthetic intern records |
| Features | Completion Time, Feedback Rating, Attendance |
| Target | Performance Score (0-100) |
| Models | Random Forest & XGBoost |
| Best R2 | 0.61 ✅ |
| Best MAE | 7.51 |

---

## 🗂️ Project Structure
```
├── app.py                        → Streamlit UI
├── model.pkl                     → Trained XGBoost model
├── scaler.pkl                    → MinMax Scaler
├── intern_dataset_realistic.csv  → Dataset
└── requirements.txt              → Dependencies
```

---

## 🔄 Project Journey

### Step 1 — Dataset Creation
- Generated 10,000 synthetic intern records
- Injected real world imperfections:
  - ❌ Noise & typos in attendance
  - 📅 Life event drops
  - ⚖️ Manager bias in feedback ratings
  - 🔀 Natural inconsistency
  - ❓ 2% missing values

### Step 2 — Data Cleaning
- ✅ Checked data types & info
- ✅ Handled missing values (Mean Imputation)
- ✅ Handled outliers (kept informative ones)
- ✅ Removed duplicates (0 found)
- ✅ Applied MinMax Feature Scaling

### Step 3 — Model Building & Results
| Model | MAE | R2 Score |
|-------|-----|----------|
| Random Forest | 7.83 | 0.57 |
| XGBoost | 7.51 | 0.61 ✅ |

### Step 4 — Feature Importance
| Feature | Importance |
|---------|------------|
| Completion Time | 0.52 🥇 |
| Feedback Rating | 0.42 🥈 |
| Attendance | 0.06 🥉 |

---

## 🚀 How To Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🛠️ Tech Stack
- Python
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Gradio
- Matplotlib & Seaborn

---

## 👤 Author
**MAhmadMakhdoom**
> Future Data Scientist | ML & AI Enthusiast

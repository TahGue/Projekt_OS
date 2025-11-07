# Quick Reference Guide - Olympic Games Data Analysis

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run EDA
```bash
# Option 1: Jupyter Notebook
jupyter notebook notebooks/01_exploratory_analysis.ipynb

# Option 2: Python Script
cd notebooks
python 01_exploratory_analysis.py
```

### 3. Run Dashboard
```bash
python -m src.dashboard
# Or
cd src
python dashboard.py
```
Then open: `http://localhost:8050`

## 📁 Project Structure

```
osproject/
├── data/
│   └── athlete_events.csv          # Main dataset
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb  # EDA notebook
│   └── 01_exploratory_analysis.py     # EDA script
├── src/
│   ├── data_loader.py              # Data loading + anonymization
│   ├── data_processor.py           # OlympicAnalyzer class
│   └── dashboard.py                 # Plotly Dash app
├── assets/
│   └── style.css                   # Dashboard styling
├── figures/                        # Generated visualizations
├── requirements.txt                # Dependencies
├── Procfile                        # Deployment config
├── README.md                       # Full documentation
├── PROJECT_CHECKLIST.md            # Task checklist
├── VIDEO_SCRIPT.md                 # Video script (Task 4)
└── QUICK_REFERENCE.md             # This file
```

## ✅ Task Completion Status

| Task | Status | Files |
|------|--------|-------|
| Task 0: EDA | ✅ Complete | `notebooks/01_exploratory_analysis.*` |
| Task 1: Country Stats | ✅ Complete | `src/data_loader.py`, `src/data_processor.py`, `src/dashboard.py` |
| Task 2: Sport Stats | ✅ Complete | `src/data_processor.py`, `src/dashboard.py` |
| Task 3: Dashboard | ✅ Complete | `src/dashboard.py`, `assets/style.css` |
| Task 4: Video | 📝 Script Ready | `VIDEO_SCRIPT.md` |

## 🔑 Key Features

### GDPR Compliance
- ✅ SHA-256 name anonymization
- ✅ Original names removed
- ✅ Hash-based identification

### Code Quality
- ✅ OOP structure (OlympicAnalyzer class)
- ✅ Modular design (separate modules)
- ✅ Well-commented code
- ✅ Descriptive variable names

### Visualizations
- ✅ Interactive Plotly Dash dashboard
- ✅ Country statistics (Task 1)
- ✅ Sport statistics (Task 2)
- ✅ Unified design with CSS

## 📊 Dashboard Features

### Task 1: Country Statistics (Kanada)
- Top sports by medals (horizontal bar chart)
- Medals per Olympics (line chart)
- Age distribution (histogram)
- Medal types distribution (pie chart)

### Task 2: Sport Statistics
- Medal distribution by country (bar chart)
- Age distribution (histogram)
- Gender distribution (pie chart)
- Medal types distribution (pie chart)

## 🎥 Video Recording Checklist

- [ ] Read `VIDEO_SCRIPT.md`
- [ ] Test dashboard locally
- [ ] Have GitHub repo open
- [ ] Have code editor open
- [ ] Test screen recording software
- [ ] Record 5-10 minute video
- [ ] Upload to video platform
- [ ] Add link to submission

## 📝 Submission Requirements

- [ ] GitHub repository link
- [ ] Deployed Dash app link (Render/Heroku)
- [ ] Individual video link (Task 4)
- [ ] All code sources cited (if applicable)

## 🔗 Important Links

- **Dataset**: https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
- **Plotly Dash Docs**: https://dash.plotly.com/
- **Pandas Docs**: https://pandas.pydata.org/docs/

## 💡 Tips

1. **For Deployment**: Use Render or Heroku with the provided `Procfile`
2. **For Video**: Follow the script in `VIDEO_SCRIPT.md` for best results
3. **For Git**: Make several meaningful commits as you develop
4. **For Code**: Use technical language in video for "Väl Godkänt" grade


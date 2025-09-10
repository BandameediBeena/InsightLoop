# InsightLoop 🌀  
**AI-Based Daily Routine Tracker and Visualizer**  

InsightLoop helps you track, analyze, and visualize your daily routines using AI.  
It identifies behavioral patterns, generates weekly reports, and provides meaningful insights into your activities with interactive charts and summaries.  

---

## ✨ Features  
- 📊 **Routine Tracking** – Log daily tasks and habits.  
- 🤖 **AI Analysis** – Detects hidden patterns in your routine.  
- 📈 **Charts & Visuals** – Generates graphs for productivity, focus, and time usage.  
- 📝 **Weekly Reports** – Automatic text reports for reviewing progress.  
- 🔄 **Custom Modules** – Easy to extend with new trackers.  

---

## 📂 Project Structure  
```

InsightLoop/
│── charts/              # Generated charts
│── config/              # Configuration files
│── logs/                # Activity and error logs
│── modules/             # Core analysis modules
│── reports/             # Generated reports
│── visuals/             # Visual assets (charts, images)
│── generate\_charts.py   # Script for chart generation
│── main.py              # Main entry point
│── report\_generator.py  # Weekly report generator
│── weekly\_report.txt    # Sample generated report
│── y.py                 # Utility / experimental script

````

---

## 🛠 Requirements  
- Python 3.8+  
- Libraries:  
  ```bash
  pip install matplotlib pandas numpy
````

---

## 🚀 Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/BandameediBeena/InsightLoop.git
   cd InsightLoop
   ```

2. **Run Main Program**

   ```bash
   python main.py
   ```

3. **Generate Charts**

   ```bash
   python generate_charts.py
   ```

4. **Generate Weekly Report**

   ```bash
   python report_generator.py
   ```

Reports will be saved in the `reports/` folder, and charts will be in `charts/` or `visuals/`.

---

## 📊 Example Output

* **Weekly Report (Text)** → insights on routines & patterns.
* **Charts** → productivity trends, task distribution, focus times.




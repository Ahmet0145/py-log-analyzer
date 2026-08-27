# 🛡️ Python Log Analyzer & Brute-Force Detector

A lightweight Python security automation tool designed to analyze server authentication logs, detect brute-force login attempts using custom thresholds, and generate structured security reports.

## 🚀 Features
- **Log Parsing:** Filters failed login attempts (`FAIL`) from standard server log files.
- **Threat Detection:** Tracks attempt counts per IP address and triggers an `[ALERT]` when attempts cross a set threshold.
- **Colored CLI Output:** Integrates `colorama` for quick terminal visual inspection.
- **Automated Reporting:** Outputs structured analysis logs directly to a `rapor.txt` report file.

## 🛠️ Requirements & Installation
```bash
pip install colorama
```

## 💻 Usage
Run the analysis script via terminal:
```
python analiz.py
```

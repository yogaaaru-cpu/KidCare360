# KidCare 360 — Working Streamlit Prototype

**Tagline:** The Right Information at the Right Time

## What this prototype includes
- Dashboard with student search and grade filter
- Emergency View with the five project fields
- Privacy & Safety explanation
- Testing Log to record actual usability-test results
- Five fictional sample student records
- No camera/video capture, external API, database, or cloud storage

## Important
This is an educational demonstration, not a production medical-record system. Do not enter real student health information. The sample data is fictional. The app has no real authentication; do not publish it publicly or use it for real emergencies.

## Run on Windows
1. Install Python 3.11 from the official Python website if it is not already installed.
2. Extract this ZIP to a folder such as `Documents\KidCare360`.
3. Open that folder in VS Code.
4. Open **Terminal → New Terminal**.
5. Run these commands, one at a time:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

If PowerShell blocks activation, try Command Prompt in VS Code and run:
```bat
.venv\Scripts\activate.bat
```
Then install requirements and run Streamlit as above.

6. A browser page should open. If not, copy the local URL shown in the terminal (usually `http://localhost:8501`) into your browser.
7. Use the sidebar to visit Dashboard, Emergency View, Privacy & Safety, and Testing Log.
8. Capture screenshots of the actual running app. Do not use real student data.

## Screenshot checklist for the PPT
1. Dashboard — show the search box, sample student list, and demo metrics.
2. Emergency View — show all five health fields for one fictional student.
3. Privacy & Safety — show the local demo-data/privacy statements.

## Suggested test
Ask 3–5 volunteers to find a named fictional student and locate the allergy and guardian-contact fields. Record the real results, feedback, and improvements. Never claim a result that was not measured.

## If `py -3.11` does not work
Run `py --list` to check installed Python versions. If Python 3.11 is installed, use its listed launcher version. Avoid changing a working Python installation unnecessarily.

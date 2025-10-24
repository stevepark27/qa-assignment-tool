# QA Assignment Tool

A Python-based automation tool that helps QA managers automatically assign representatives to qualified team leads for monthly evaluations.  
It replaces a time-consuming manual process with an intelligent, repeatable system that ensures balanced, fair, and varied workload distribution.

---

## 🧩 Project Overview

The **QA Assignment Tool** was developed to support a QA manager who manually assigned over 200 representatives each month to team leads for quality evaluations — a process that took about two hours every month.  
This tool automates the process, ensuring assignments are fair, qualification-based, and rotated to prevent repetitive pairings.

---

## 🎯 Problem Statement

- Over 200 representatives required monthly QA evaluations.  
- Each team lead specialized in specific call types.  
- The **QA manager** manually matched reps to team leads in Excel.  
- The process was time-consuming and difficult to balance evenly.  
- The manager wanted a faster, fairer, and more automated solution that also promoted rotation.

---

## 💡 Solution

The tool automates and randomizes the assignment process using Python:
- Reads representative and team lead data directly from **Excel workbooks (.xlsx)**.  
- Groups reps by call type and distributes them evenly among qualified leads.  
- Includes a **shuffling system** that increases the likelihood of reps being assigned to different leads each month.  
- Writes the final results to a new Excel sheet, ready for review or sharing.  

This automation reduced a two-hour manual task to **less than one minute** while improving consistency and fairness.

---

## ⚙️ How It Works

1. **Input file**:  
   - `qa_assignments.xlsx` – contains multiple sheets:
     - `Reps` – list of representatives and their qualified call types  
     - `Leads` – list of team leads and their specializations  

2. **Script execution**:
   ```bash
   python qa_assignment_tool.py

3. Output:

A new sheet (e.g., Assignments) added to the same workbook, showing the final mapping of reps to team leads, evenly distributed and randomized.


---

🧠 Key Features

Automated assignment generation

Qualification-based matching

Shuffling system for monthly rotation

Direct Excel (.xlsx) read/write

Configurable assignment rules

Transparent, reproducible, and fair results



---

📈 Impact

Reduced manual workload from 2 hours to under 1 minute

Improved fairness and consistency of assignments

Promoted monthly variation to avoid repetition

Increased efficiency and transparency for the QA manager



---

🧰 Tech Stack

Python (pandas, openpyxl, random)

Excel (.xlsx) integration for input/output

Optional: Streamlit UI (for future dashboard)


---

🚀 Future Enhancements

Add a Streamlit interface for uploading spreadsheets and previewing results

Include historical tracking to prevent repeating prior assignments

Integrate notifications for QA managers upon completion


---

👤 Author

Steve Soll
📍 Based in France | US Citizen
💼 LinkedIn Profile https://www.linkedin.com/in/steve-solnosky-data27/
💻 GitHub Profile

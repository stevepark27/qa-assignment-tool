# QA Assignment Tool

A Python-based automation tool that helps QA managers automatically assign representatives to qualified team leads for monthly evaluations.  
It replaces a time-consuming manual process with an intelligent, repeatable system that ensures balanced, fair, and varied workload distribution.

---

## 🧩 Project Overview

The **QA Assignment Tool** was developed to support a QA manager who manually assigned over 200 representatives each month to team leads for quality evaluations — a process that took about two hours every month.  
This tool automates the process, ensuring assignments are fair, qualification-based, and rotated over time to prevent repetitive pairings while balancing workloads.

---

## 🎯 Problem Statement

- Over 200 representatives required monthly QA evaluations.  
- Each team lead specialized in specific call types.  
- The **QA manager** manually matched reps to team leads in Excel.  
- Some leads had many more qualifications than others, making workload balancing difficult.  
- The manager wanted a faster, fairer, and more automated solution that also promoted rotation.

---

## 💡 Solution

The tool automates and balances the assignment process using Python:
- Reads representative and team lead data directly from **Excel workbooks (.xlsx)**.  
- Groups reps by call type and distributes them evenly among qualified leads.  
- Uses a **maximum hours variable** to prevent overloading highly qualified leads while maintaining balanced distribution.  
- Includes a **shuffling system** that increases the likelihood of reps being assigned to different leads each month.  
- Writes the final results to a new Excel sheet, ready for review or sharing.  

This automation reduced a two-hour manual task to **less than one minute** while improving fairness, transparency, and workload balance.

---

## ⚙️ How It Works

1. **Input file**:  
   - `QA_Assignments.xlsx` – contains multiple sheets:
     - `Reps` – list of representatives, their qualified call types, and their required hours of evaluation 
     - `Leads` – list of team leads, their specializations, and the maximum hours to be assigned 

2. **Script execution**:
   ```bash
   python QA_assignment_project.py

3. Output:

Three new sheets (Assignments, Unassigned Reps, and Lead Hour Balance) showing the final mapping of reps to team leads, any unassigned reps, and remaining Lead hours.





---

🧠 Key Features

Automated assignment generation

Qualification-based matching

Max hours variable for balanced workloads

Shuffling system for monthly rotation

Direct Excel (.xlsx) read/write

Configurable assignment rules

Transparent, reproducible, and fair results



---

📈 Impact

Reduced manual workload from 2 hours to under 1 minute

Improved fairness and consistency of assignments

Balanced workloads even when leads have different qualification levels

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

Steve Solnosky
📍 Based in France | US Citizen
💼 LinkedIn Profile https://www.linkedin.com/in/steve-solnosky-data27/

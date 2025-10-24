# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 17:39:39 2025

@author: steve
"""

import pandas as pd
from sklearn.utils import shuffle

# Import Data

rep_df = pd.read_excel("data/QA_Assignments.xlsm", sheet_name=2)
lead_df = pd.read_excel("data/QA_Assignments.xlsm", sheet_name=7)

# Shuffle data
rep_df = shuffle(rep_df)

# Function to assign reps to team leads
def assign_reps_to_leads(rep_df, lead_df):
    assignments = []
    
    for index, rep_row in rep_df.iterrows():
        rep = rep_row['Rep Name']
        rep_hours = rep_row['Eval Hrs']
        rep_call_types = rep_row.drop(['Rep Name', 'Eval Hrs'])
        
        for lead_index, lead_row in lead_df.iterrows():
            lead = lead_row['Team Lead']
            lead_max_hours = lead_row['Max Hours']
            lead_call_types = lead_row.drop(['Team Lead', 'Max Hours'])
            
            if all(rep_call_types <= lead_call_types) and rep_hours <= lead_max_hours:
                assignments.append({'Rep Name': rep, 'Team Lead': lead, 'Eval Hrs': rep_hours})
                lead_df.at[lead_index, 'Max Hours'] -= rep_hours
                break
    
    return pd.DataFrame(assignments)

# Assign reps to team leads
assignments_df = assign_reps_to_leads(rep_df, lead_df)

# print(assignments_df)

# Find unassigned reps
unassigned_reps = rep_df[~rep_df['Rep Name'].isin(assignments_df['Rep Name'])]

# Create Excel Output for User
with pd.ExcelWriter('data/QA_Assignment_Results.xlsx') as writer:
    assignments_df.to_excel(writer, sheet_name = 'Assignments', index = False)
    unassigned_reps.to_excel(writer, sheet_name = 'Unassigned Reps', index = False)
    lead_df.to_excel(writer, sheet_name = 'Lead Hour Balance', index = False)



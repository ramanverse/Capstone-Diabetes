import pandas as pd
import numpy as np
import os

def run_etl():
    print("Starting ETL Pipeline...")
    
    # 1. Extraction
    raw_path = 'data/raw/diabetic_data.csv'
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found.")
        return
        
    df = pd.read_csv(raw_path)
    cols = ['encounter_id', 'patient_nbr', 'race', 'gender', 'age', 
            'time_in_hospital', 'num_medications', 'num_lab_procedures', 
            'number_diagnoses', 'admission_type_id', 'discharge_disposition_id', 
            'insulin', 'diabetesMed', 'readmitted']
    df = df[cols].copy()
    
    # 2. Cleaning
    df.replace('?', np.nan, inplace=True)
    df = df[df['gender'] != 'Unknown/Invalid']
    df = df[df['discharge_disposition_id'] != 11] # Remove expired
    df['race'].fillna(df['race'].mode()[0], inplace=True)
    
    # Age to midpoint
    age_map = {'[0-10)': 5, '[10-20)': 15, '[20-30)': 25, '[30-40)': 35, 
               '[40-50)': 45, '[50-60)': 55, '[60-70)': 65, '[70-80)': 75, 
               '[80-90)': 85, '[90-100)': 95}
    df['age_midpoint'] = df['age'].map(age_map)
    
    # Target encoding
    df['readmitted_binary'] = df['readmitted'].apply(lambda x: 1 if x == '<30' else 0)
    
    # Deduplication
    df = df.sort_values('encounter_id').drop_duplicates(subset='patient_nbr', keep='first')
    
    # 3. Export
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/diabetes_cleaned.csv', index=False)
    print(f"ETL Complete. Processed {len(df)} records.")

if __name__ == "__main__":
    run_etl()

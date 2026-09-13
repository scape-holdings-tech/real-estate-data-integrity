import pandas as pd
import numpy as np

# ==============================================================================
# SCAPE HOLDINGS LLC — PROPERTY TECH & DATA OPERATIONS DIVISION
# SYSTEM 2: AUTOMATED REAL ESTATE LEAD-CLEANSING & PIPELINE INFRASTRUCTURE
# DESIGNED FOR: Real Estate Syndicates, Private Equity Funds, & Elite Realtors
# ==============================================================================

def run_lead_pipeline_optimization():
    print("Initializing Scape Holdings Real Estate Data Cleanse Engine...\n")
    
    # Generate mock chaotic investor lead data
    mock_investor_data = {
        'Property_Address': ['123 n central ave', '456 E CAMELBACK RD', '123 N Central Ave ', '789 w indian school rd', '789 W Indian School Rd', '555 S Oracle Rd'],
        'Owner_First_Name': ['john', 'SARAH', 'John', 'michael', 'Michael', 'Rebecca'],
        'Owner_Last_Name': ['smith', 'JONES', 'Smith', 'brown', 'Brown', 'Davis'],
        'Estimated_Market_Value': [450000.00, np.nan, 450000.00, 320000.00, 320000.00, np.nan], 
        'Contact_Phone_Status': ['Verified', 'Verified', 'Verified', 'Disconnected', 'Disconnected', 'Verified']
    }
    raw_leads = pd.DataFrame(mock_investor_data)

    print("--- [RAW PROPERTY LEAD INITIAL DATA SCAN] ---")
    print(raw_leads)
    print(f"\nTotal Raw Properties Ingested: {len(raw_leads)}\n")
    print("--------------------------------------------------------------------------")
    print("EXECUTING LEAD PIPELINE DATA OPTIMIZATION...")
    print("--------------------------------------------------------------------------")

    # QA PROTOCOL 1: STRIP WHITESPACE & STANDARDIZE STRING CASING
    raw_leads['Property_Address'] = raw_leads['Property_Address'].str.strip().str.upper()
    print("[QA STATUS 1] Success. All address fields normalized to UPPERCASE block structures.")

    # QA PROTOCOL 2: PURGE SYSTEMIC DUPLICATE PROPERTY RECORDS
    cleaned_leads = raw_leads.drop_duplicates(subset=['Property_Address'], keep='first').copy()
    duplicates_purged = len(raw_leads) - len(cleaned_leads)
    print(f"[QA STATUS 2] Success. Database scrubbing identified and purged {duplicates_purged} duplicate listings.")

    # QA PROTOCOL 3: PROPERTY VALUE VALIDATION & NULL ISOLATION
    cleaned_leads['Estimated_Market_Value'] = cleaned_leads['Estimated_Market_Value'].fillna(0.00)
    print("[QA STATUS 3] Success. Missing financial evaluations resolved and set to 0.00 baseline.")

    # QA PROTOCOL 4: STRING DATA MERGING & FIELD CONSOLIDATION
    cleaned_leads['Owner_First_Name'] = cleaned_leads['Owner_First_Name'].str.capitalize()
    cleaned_leads['Owner_Last_Name'] = cleaned_leads['Owner_Last_Name'].str.capitalize()
    cleaned_leads['Mailing_Contact'] = cleaned_leads['Owner_First_Name'] + " " + cleaned_leads['Owner_Last_Name']
    cleaned_leads = cleaned_leads.drop(columns=['Owner_First_Name', 'Owner_Last_Name'])
    print("[QA STATUS 4] Success. Field consolidation complete. Generated unified 'Mailing_Contact' rows.")

    print("\n==============================================================================")
    print("SCAPE HOLDINGS LLC: FINAL CLEANED PROPERTY MARKETING DATASET")
    print("==============================================================================")
    print(cleaned_leads.to_string(index=False))
    print("==============================================================================")

# Execute the software system
run_lead_pipeline_optimization()

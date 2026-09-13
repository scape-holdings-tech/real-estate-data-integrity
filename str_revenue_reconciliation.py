import pandas as pd
import numpy as np

# ==============================================================================
# SCAPE HOLDINGS LLC — SHORT-TERM RENTAL FINANCIAL OPERATIONS
# SYSTEM 3: STR REVENUE RECONCILIATION & API INTEGRATION AUDITOR
# DESIGNED FOR: Multi-Property Airbnb Investors & Large Hospitality Networks
# ==============================================================================

def execute_revenue_reconciliation():
    print("Initializing Scape Holdings Financial Leak Auditing Engine...\n")
    
    # Generate mock cross-platform data environments for verification
    print("Standalone simulation environments activated. Ingesting disparate platform logs...")
    
    # Table 1: Ingested Bank Records from Airbnb Booking Revenue
    mock_payouts = {
        'Reservation_ID': ['RES-8821', 'RES-8822', 'RES-8823', 'RES-8824'],
        'Actual_Net_Payout': [420.00, 510.50, 190.00, 680.00]
    }
    # Table 2: Automated Dynamic Pricing Telemetry (e.g., PriceLabs API Feed)
    mock_pricing = {
        'Reservation_ID': ['RES-8821', 'RES-8822', 'RES-8823', 'RES-8824'],
        'Expected_Net_Revenue': [420.00, 650.00, 190.00, 720.00] # Communication disconnects present
    }
    actual_payouts = pd.DataFrame(mock_payouts)
    expected_pricing = pd.DataFrame(mock_pricing)

    print("\n--- [RAW INGESTED AIRBNB PAYOUT TABLE] ---")
    print(actual_payouts.to_string(index=False))
    print("\n--- [RAW PRICELABS DYNAMIC API LOGS] ---")
    print(expected_pricing.to_string(index=False))
    print("\n--------------------------------------------------------------------------")
    print("EXECUTING FINANCIAL RECORD MATCHING & VARIANCE AUDIT...")
    print("--------------------------------------------------------------------------")

    # QA PROTOCOL 1: ADVANCED MULTI-SOURCE TABLE MERGING (SQL JOIN Equivalent)
    # We join both separate tables securely on their shared unique Reservation ID.
    merged_ledger = pd.merge(actual_payouts, expected_pricing, on='Reservation_ID', how='inner')
    print("[QA STATUS 1] Success. Platform datasets merged via relational matrix.")

    # QA PROTOCOL 2: PROGRAMMATIC VARIANCE CALCULATION
    # Automatically subtract actual payouts from expected figures to scan for capital leakage.
    merged_ledger['Revenue_Leakage'] = merged_ledger['Expected_Net_Revenue'] - merged_ledger['Actual_Net_Payout']
    print("[QA STATUS 2] Success. Account ledger calculations executed.")

    # QA PROTOCOL 3: ANOMALY FILTERING
    # Isolate and display only the exact rows where software communication sync failures cost money.
    leakage_report = merged_ledger[merged_ledger['Revenue_Leakage'] > 0.00].copy()
    print(f"[QA STATUS 3] Complete. Identified {len(leakage_report)} active API ingestion drops.")

    print("\n==============================================================================")
    print("SCAPE HOLDINGS LLC: COMPLIANCE EXCEPTION REPORT (FLAGGED CAPITAL LEAKS)")
    print("==============================================================================")
    if leakage_report.empty:
        print("Flawless System Interoperability Verified. 0 Leaks Found.")
    else:
        print(leakage_report.to_string(index=False))
    print("==============================================================================")

# Execute the software system
execute_revenue_reconciliation()

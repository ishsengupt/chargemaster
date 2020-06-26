import csv
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE healthcareComp(
    id integer PRIMARY KEY,
    CDM_Description text,
    CHARGE_CODE text,
    CPTHCPCS text,
    CPT4_Code text,
    Charge_Category text,
    Charge_Code_Alt text,
    Charge_Dept_ID text,
    Charge_Dept_Name text,
    ChargeCode text,
    Comments text,
    Description text,
    EAP text,
    Effective_Date text,
    GroupName text,
    HCPCS text,
    HCPCS_Code text,
    HSP text,
    Hospital text,
    IVDESC text,
    IVNUM text,
    IVREVCD text,
    Inpatient_Price text,
    Name text,
    Outpatient_Price text,
    Price text,
    Procedure_Code text,
    Procedure_Desc text,
    Procedure_Effective_Date text,
    PxRxSx text,
    QUANTITY text,
    REV text,
    Rev_Code text,
    Revenue_Center text,
    Revenue_Code text,
    Std_Price text,
    TYPE text,
    UB_Revenue_Code text,
    UNITS text,
    UNIT_PRICE text,
    Year text,
    CDM_Number__CDM_Code text
        )
        """)
conn.commit()

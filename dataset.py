import pandas as pd

resumes = pd.DataFrame({
    "name": ["Alice","Bob","Navya"],
    "skills": ["python, sql, machine learning",
               "excel, sql",
               "python, excel"],
    "experience": [3,1,2]
})
print("Resumes DataFrame:")
print(resumes)
resumes.to_csv(r"d:\java\BINARY BRAINS\resumes.csv", index=False)
print("✓ resumes.csv saved successfully\n")

leave = pd.DataFrame({
    "employee": ["Navya","Alice"],
    "role": ["developer","intern"],
    "team": ["alpha","beta"],
    "leave_balance": [10,5],
    "start_date": ["2026-02-10","2026-02-15"],
    "end_date": ["2026-02-12","2026-02-16"]
})
print("Leave DataFrame:")
print(leave)
leave.to_csv(r"d:\java\BINARY BRAINS\leave_data.csv", index=False)
print("✓ leave_data.csv saved successfully")
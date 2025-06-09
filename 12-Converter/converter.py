import pandas as pd

# Load the Excel file
excel_file = '/Users/phamthanh/Downloads/6a2.xlsx'

# Read the sheet
df = pd.read_excel(excel_file)

# Save to CSV
df.to_csv('6a2.csv', index=False)

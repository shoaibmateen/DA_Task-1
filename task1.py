import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Preview basic info
print(df.head())
print(df.columns)
print(df.info())
print(df.describe(include='all'))

# Fill missing values (basic forward fill as placeholder)
df.ffill(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename columns to lowercase, remove spaces
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert date_added to datetime
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Save cleaned dataset
df.to_csv('cleaned_netflix_titles.csv', index=False)

print("✅ Cleaning complete! Saved as cleaned_netflix_titles.csv")

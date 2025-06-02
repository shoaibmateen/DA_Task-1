import pandas as pd

df = pd.read_csv('netflix_titles.csv')

print(f"Original shape: {df.shape}")
print("\nMissing values before cleaning:")
print(df.isnull().sum())

duplicates_before = df.duplicated().sum()
print(f"\nDuplicate rows before cleaning: {duplicates_before}")

df.ffill(inplace=True)
df.drop_duplicates(inplace=True)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

print(f"\nShape after cleaning: {df.shape}")
print("\nMissing values after cleaning:")
print(df.isnull().sum())

duplicates_after = df.duplicated().sum()
print(f"\nDuplicate rows after cleaning: {duplicates_after}")

df.to_csv('cleaned_netflix_titles.csv', index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_netflix_titles.csv'")
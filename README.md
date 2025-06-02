# Task 1 - Data Cleaning and Preprocessing

## Dataset Used:
Mall Customer Segmentation Data (Kaggle)

## Cleaning Steps:
- Removed 5 duplicate rows.
- Filled 2 missing values in 'Age' with the median.
- Standardized 'Gender' entries (e.g., "Male", "M" → "male").
- Reformatted 'Joining Date' to dd-mm-yyyy format.
- Renamed columns to snake_case (e.g., 'Annual Income (k$)' → 'annual_income_k').
- Converted 'Age' to integer and 'Joining Date' to datetime format.

## Tools:
- Python (Pandas)

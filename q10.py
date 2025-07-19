import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


file_path = "C:\\Users\\sevit\\Downloads\\Machine Learning\\ML-lab\\Session Data.xlsx" 
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')


print("First 5 rows of the dataset:")
print(df.head())


print("\n--- Data Info ---")
df.info()


print("\n--- Data Types ---")
print(df.dtypes)


categoriescolumns = df.select_dtypes(include=['object']).columns.tolist()
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

print(f"\nCategorical Columns: {categoriescolumns}")
print(f"Numeric Columns: {numeric_cols}")


print("\n--- Unique values in categorical columns ---")
for col in categoriescolumns:
    print(f"{col}: {df[col].unique()}")

print("\n--- Missing Values ---")
print(df.isnull().sum())


print("\n--- Summary Statistics for Numeric Columns ---")
print(df[numeric_cols].describe())


print("\n--- Mean and Variance ---")
for col in numeric_cols:
    print(f"{col}: Mean = {df[col].mean():.2f}, Variance = {df[col].var():.2f}")

print("\n--- Boxplots for Outlier Detection ---")
for col in numeric_cols:
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot for {col}')
    plt.show()


print("\n--- Encoding Suggestion ---")
for col in categoriescolumns:
    unique_vals = df[col].unique()
    print(f"{col} - Unique values: {unique_vals}")
    print(f"-> Suggested encoding: {'Label Encoding (Ordinal)' if sorted(unique_vals.tolist()) == unique_vals.tolist() else 'One-Hot Encoding (Nominal)'}\n")


df_encoded = df.copy()
le = LabelEncoder()
for col in categoriescolumns:
    df_encoded[col] = le.fit_transform(df[col].astype(str))

print("\n--- Encoded Data Sample ---")
print(df_encoded.head())
import pandas as pd


file_path = "C:\\Users\\sevit\\Downloads\\Machine Learning\\ML-lab\\Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')
df = df.replace({'t':1,'f':0})  

vector1 = df.iloc[0]
vector2 = df.iloc[1]


binarycolumns = [col for col in df.columns if set(df[col].dropna().unique()).issubset({0, 1})]

print(f"\nBinary columns: {binarycolumns}")

v1 = vector1[binarycolumns].astype(int)
v2 = vector2[binarycolumns].astype(int)


f11 = ((v1 == 1) & (v2 == 1)).sum()
f00 = ((v1 == 0) & (v2 == 0)).sum()
f10 = ((v1 == 1) & (v2 == 0)).sum()
f01 = ((v1 == 0) & (v2 == 1)).sum()


jc = f11 / (f11 + f10 + f01) if (f11 + f10 + f01) > 0 else 0


smc = (f11 + f00) / (f11 + f00 + f10 + f01)

print("\n--- Similarity Measures ---")
print(f"f11 (1 in both): {f11}")
print(f"f00 (0 in both): {f00}")
print(f"f10 (1 in vector1, 0 in vector2): {f10}")
print(f"f01 (0 in vector1, 1 in vector2): {f01}")
print(f"Jaccard Coefficient: {jc:.4f}")
print(f"Simple Matching Coefficient: {smc:.4f}")


print("\n--- Interpretation ---")
if jc < smc:
    print("SMC is higher because it considers both agreements: 0s and 1s.")
    print("JC is stricter, useful when 1s represent meaningful presence (e.g., symptom ON).")
else:
    print("JC and SMC are close; dataset has more agreement on 1s or few disagreements overall.")
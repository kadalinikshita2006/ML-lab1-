import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


file_path = "C:\\Users\\sevit\\Downloads\\Machine Learning\\ML-lab\\Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')


vector1 = df.iloc[0].values.reshape(1, -1)
vector2 = df.iloc[1].values.reshape(1, -1)


df_encoded = pd.get_dummies(df)


vector1_enc = df_encoded.iloc[0].values.reshape(1, -1)
vector2_enc = df_encoded.iloc[1].values.reshape(1, -1)


cos_sim = cosine_similarity(vector1_enc, vector2_enc)[0][0]

print(f"Cosine Similarity between vector 1 and vector 2: {cos_sim:.4f}")
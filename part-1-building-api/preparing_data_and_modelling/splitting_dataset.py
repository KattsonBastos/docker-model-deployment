import pandas as pd

df = pd.read_csv('../data/cardio_train.csv', sep=';')

df_1 = df[df['cardio'] == 0][['age', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'cardio']].sample(5000)
df_2 = df[df['cardio'] == 1][['age', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'cardio']].sample(5000)
df = pd.concat([df_1, df_2], ignore_index=True)

print(df.shape)

df.to_csv('../data/cardio_train_sampled.csv', index=False)
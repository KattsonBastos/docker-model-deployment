import os
import pickle

import pandas       as pd

from lightgbm                import LGBMClassifier
from sklearn.metrics         import accuracy_score
from sklearn.preprocessing   import MinMaxScaler
from sklearn.model_selection import train_test_split

# loading the data
df = pd.read_csv('../data/cardio_train_sampled.csv')

# changing age from days into years
df['age'] = round(df['age'] / 365).astype(int)

print(df.head())

# splitting data into train and test
X = df.drop('cardio', axis =1)
y = df['cardio'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

# Data Preparation

## scaling
mm_age = MinMaxScaler()
mm_weight = MinMaxScaler()
mm_ap_hi = MinMaxScaler()
mm_ap_lo = MinMaxScaler()

X_train['age'] = mm_age.fit_transform(X_train[['age']].values)
pickle.dump( mm_age, open( '../parameters/age_scaler.pkl', 'wb') )

X_train['weight'] = mm_weight.fit_transform(X_train[['weight']].values)
pickle.dump( mm_weight, open( '../parameters/weight_scaler.pkl', 'wb') )

X_train['ap_hi'] = mm_ap_hi.fit_transform(X_train[['ap_hi']].values)
pickle.dump( mm_ap_hi, open( '../parameters/ap_hi_scaler.pkl', 'wb') )

X_train['ap_lo'] = mm_ap_lo.fit_transform(X_train[['ap_lo']].values)
pickle.dump( mm_ap_lo, open( '../API/parameters/ap_lo_scaler.pkl', 'wb') )

# scaling test dataset
X_test['age'] = mm_age.transform(X_test[['age']].values)
X_test['weight'] = mm_weight.transform(X_test[['weight']].values)
X_test['ap_hi'] = mm_ap_hi.transform(X_test[['ap_hi']].values)
X_test['ap_lo'] = mm_ap_lo.transform(X_test[['ap_lo']].values)

X_train = X_train.values
X_test = X_test.values

# Modelling
lgbm = LGBMClassifier(random_state = 42).fit(X_train, y_train)

# prediction
yhat_lgbm= lgbm.predict( X_test )

print(accuracy_score(y_test, yhat_lgbm))

pickle.dump(lgbm, open( os.path.join('../models', "model.pkl"), "wb" )) 
import pandas as pd

from config           import results
from tools.file_tools import load_pickle

class PredictionTools:
    
    def __init__(self):

        self.results = results

        self.mm_age = load_pickle(f"../parameters/age_scaler.pkl")

        self.mm_weight = load_pickle(f"../parameters/weight_scaler.pkl")

        self.mm_ap_hi = load_pickle(f"../parameters/ap_hi_scaler.pkl")
        
        self.mm_ap_lo = load_pickle(f"../parameters/ap_lo_scaler.pkl")

        self.model = load_pickle("../models/model.pkl")


    def data_preparation(self, data):
        """Receives the data as a dictionary and preprocess them
        :param data: a dictionary containing data regardinh to each variable used in the training and prediction
        :returns: the data preprocessed as a Pandas Dataframe """

        data = pd.DataFrame(data)

        # data manipulation and feature engineering (in this simple example, we only change age from days to years)
        data['age'] = round(data['age'] / 365).astype(int)
        
        # scaling step
        data['age'] = self.mm_age.transform(data[['age']].values)

        data['weight'] = self.mm_weight.transform(data[['weight']].values)

        data['ap_hi'] = self.mm_ap_hi.transform(data[['ap_hi']].values)

        data['ap_lo'] = self.mm_ap_lo.transform(data[['ap_lo']].values)

        return data


    def predict(self, df):
        """Receives a dataframe and perform the prediction.
        :param df: dataframe containing data used to make the predictions
        :returns: string with description of the result:
            - Patient without CVD
            - Patien with CVD"""

        prediction = int(self.model.predict( df.values )[0]) # predicting and converting the int result into string

        prediction = results[prediction] # getting the respective descrition for the prediction

        return prediction

    
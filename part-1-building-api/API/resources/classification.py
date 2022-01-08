from flask                  import request
from flask_restful          import Resource
from tools.prediction_tools import PredictionTools

class Classification(Resource):
    def post(self):
        data = request.json # getting the data sent

        tools = PredictionTools() # creating an object of the class we built to process and model data

        df = tools.data_preparation(data) # preprocessing the data

        prediction = tools.predict(df) # making the prediction

        
        return {"result": prediction}


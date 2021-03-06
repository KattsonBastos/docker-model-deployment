from flask                      import Flask
from flask_restful              import Api
from resources.classification   import Classification


app = Flask(__name__)

api = Api(app)

api.add_resource(Classification, '/cvd-classification')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port= 8000)

    
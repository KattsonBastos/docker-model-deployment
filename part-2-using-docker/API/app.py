from flask                      import Flask
from flask_restful              import Api
from resources.classification   import Classification
from resources.home_page        import HomePage


app = Flask(__name__)

api = Api(app)


api.add_resource(HomePage, '/home')
api.add_resource(Classification, '/cvd-classification')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 8001)

    
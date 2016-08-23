# This is the registry
# ---
# Register registers objects based on initial object receipt

from flask import Flask
from flask_restful import Api

from controllers.registry import RegisterController

app = Flask(__name__)
api = Api(app)

api.add_resource(RegisterController, '/register')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5050,
        debug=True)

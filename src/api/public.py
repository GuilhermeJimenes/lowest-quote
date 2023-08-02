from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from src.api.payload import webscraping_ns
from src.api.resources import Webscraping

print("public")

# configs
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# namespaces
api.add_namespace(webscraping_ns)

# resources
webscraping_ns.add_resource(Webscraping, "")

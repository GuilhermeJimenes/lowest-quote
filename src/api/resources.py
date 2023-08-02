from flask import request
from flask_restx import Resource

from src.api.http_response import HttpResponse
from src.api.payload import webscraping_ns, payload
from src.web_scraping.automation import Automation


class Webscraping(Resource):
    @webscraping_ns.expect(payload, validate=True)
    def post(self):
        data = request.get_json()

        response = Automation(data["browser"]).start(data["date"])
        return HttpResponse.success("sucess", response)

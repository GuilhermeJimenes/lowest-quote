from datetime import datetime

from flask_restx import Namespace, fields

# Namespaces
webscraping_ns = Namespace("web-scraping")

# Payloads
payload = webscraping_ns.model("Payload", {
    "browser": fields.String(required=True, enum=["Chrome", "Firefox", "Edge", "Safari"]),
    "date": fields.DateTime(
        required=True, min=datetime.strptime("01/01/1984", "%d/%m/%Y"), example="2023-08-01"
    )
}, strict=True)

# Headers

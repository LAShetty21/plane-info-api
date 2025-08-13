from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["POST"])
def plane_info():
    url = "https://api.adsb.lol/v2/closest/48.316408/11.693400/1"

    AIRLINE_CODES = {
        "AEE": "Aegean",
        "EIN": "Air Lingus",
        "MSC": "Air Cairo",
        "ACA": "Air Canada",
        "CCA": "Air China",
        "DLA": "Air Dolomiti",
        "AEA": "Air Europa",
        "BTI": "Air Baltic",
        "AAL": "American Airlines",
        "AFR": "Air France",
        "ANA": "All Nippon Airlines",
        "AUA": "Austrian Airlines",
        "BAW": "British Airways",
        "BEL": "Buseels Airlines",
        "CPA": "Cathay Pacific",
        "CFG": "Condor",
        "CAI": "Corendon Airlines",
        "CTN": "Croatia Airlines",
        "DAL": "Delta",
        "OCN": "Discover",
        "EZY": "easyJet",
        "EJU": "easyJet Europe"
        "MSR": "Egypt Air",
        "UAE": "Emirates",
        "ETD": "Etihad",
        "EWG": "Eurowings",
        "EVA": "Eva Air",
        "FIN": "Fin Air",
        "GFA": "Gulf Air",
        "IBE": "Iberia",
        "IBY": "Ita Airways",
        "KLM": "KLM",
        "KAC": "Kuwait Airways",
        "DLH": "Lufthansa",
        "FIA": "FlyOne",
        "LHX": "Lufthansa City",
        "LGL": "Lux Air",
        "OMA": "Oman Air",
        "PGT": "Pegasus Air",
        "QTR": "Qatar Airways",
        "SVA": "Saudia",
        "SIA": "Singapore Airlines",
        "SXS": "Sun Express",
        "SWR": "Swiss",
        "THA": "Thai Airways",
        "TUI": "TUI Fly",
        "THY": "Turkish Airlines",
        "UAL": "United Airlines",
        "UZB": "Uzbekistan Airlines",
        "HVN": "Vietnam Airlines",
        "VLG": "Vueling",
        "RYR": "Ryanair"
    }

    try:
        data = requests.get(url).json()
        aircraft_list = data.get("ac", [])
        if not aircraft_list:
            speech = "No flights found."
        else:
            ac = aircraft_list[0]
            callsign = ac.get("flight") or ac.get("callsign") or "Unknown"
            aircraft_type = ac.get("t") or ac.get("type") or "Unknown"
            airline_code = callsign[:3].upper()
            airline_name = AIRLINE_CODES.get(airline_code, "Unknown Airline")
            speech = f"The aircraft is {aircraft_type} from {airline_name}."
    except Exception as e:
        speech = f"Error fetching flight data: {str(e)}"

    return jsonify({"fulfillmentText": speech})

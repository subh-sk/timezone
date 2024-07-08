from flask import Flask, request, jsonify
from datetime import datetime
import pytz
import pycountry

app = Flask(__name__)

@app.route('/')
def index():
    country = request.args.get('country')
    if country:
        try:
            tz = pytz.country_timezones[country.upper()][0]
            current_time = datetime.now(pytz.timezone(tz))
            response = {
                'country': country,
                'date': current_time.strftime('%Y-%m-%d'),
                'time': current_time.strftime('%H:%M:%S %Z%z')
            }
            example_url = f"{request.url_root}?country={country.lower()}"
            example_output = {
                'country': country.lower(),
                'date': current_time.strftime('%Y-%m-%d'),
                'time': current_time.strftime('%H:%M:%S %Z%z')
            }
            return jsonify([
                {"Example": {"format to send": example_url, "output": example_output}},
                {"Country code:": list(pytz.country_timezones.keys())},
                {"Country names:": {country.alpha_2: country.name for country in pycountry.countries}}
            ])
        except KeyError:
            return jsonify({'error': f'Country {country} not found or does not have a valid timezone.'}), 400
    else:
        example_url = f"{request.url_root}?country=<country_code>"
        example_output = {
            "Example": {
                "format to send": example_url,
                "output": {
                    "country": "country_code",
                    "date": "YYYY-MM-DD",
                    "time": "HH:MM:SS TZ+ZZZZ"
                }
            },
            "Country names:": {country.alpha_2: country.name for country in pycountry.countries}
        }
        return jsonify(example_output), 400

if __name__ == '__main__':
    app.run(debug=True)


    # ?country=india
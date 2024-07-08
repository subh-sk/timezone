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
                'time': {
                    '12_hour': current_time.strftime('%I:%M:%S %p %Z%z'),
                    '24_hour': current_time.strftime('%H:%M:%S %Z%z')
                }
            }
            return jsonify(response)
        except KeyError:
            return jsonify({'error': f'Country code {country} not found or does not have a valid .'}), 400
    else:
        example_url = f"{request.url_root}?country=country_code"
        example_output = {
            "Example": {
                "format to send": example_url,
                "output": {
                    "country": "country_code",
                    "date": "YYYY-MM-DD",
                    "time": {
                        "12_hour": "HH:MM:SS AM/PM TZ+ZZZZ",
                        "24_hour": "HH:MM:SS TZ+ZZZZ"
                    }
                }
            },
            "country_codes:": {country.alpha_2: country.name for country in pycountry.countries}
        }
        return jsonify(example_output), 400

if __name__ == '__main__':
    app.run(debug=True)


    # ?country=india

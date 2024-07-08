from flask import Flask, request, jsonify
from datetime import datetime
import pytz
import pycountry

app = Flask(__name__)

@app.route('/')
def index():
    country_code = request.args.get('country')
    if country_code:
        try:
            # Get the first timezone for the country code
            tz = pytz.country_timezones[country_code.upper()][0]
            current_time = datetime.now(pytz.timezone(tz))
            # Get the country name from the country code
            country_name = pycountry.countries.get(alpha_2=country_code.upper()).name
            response = {
                'country': country_name,
                'date': current_time.strftime('%Y-%m-%d'),
                'time': {
                    '12_hour': current_time.strftime('%I:%M:%S %p %Z%z'),
                    '24_hour': current_time.strftime('%H:%M:%S %Z%z')
                }
            }
            return jsonify(response)
        except KeyError:
            return jsonify({'error': f'Country code {country_code} not found or does not have a valid timezone.'}), 400
        except AttributeError:
            return jsonify({'error': f'Invalid country code {country_code} provided.'}), 400
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

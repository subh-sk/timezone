# Flask Timezone API

This Flask application provides an API to fetch current date and time for various countries using their ISO codes.

## Installation

1. Ensure you have Docker installed.
2. Clone this repository.

## Usage

### Running with Docker

Build the Docker image and run the container:

```bash
docker build -t timezone-api .
docker run -p 7860:7860 timezone-api
```
- The API will be accessible at http://localhost:7860.

## API Endpoints
/: Provides instructions on how to use the API and lists available endpoints.
/time?country=<country_code>: Retrieves the current date and time for a specified country.

## Dependencies
```
Flask
Requests
DateTime
PyCountry
Pytz
```

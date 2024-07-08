FROM python:3.12


WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt


RUN pip install flask  requests datetime pycountry pytz

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "7860"]
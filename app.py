import numpy as mp

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return(
        f"Welcome to the Climate App homepage!<br>"
        f"Here are the available routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/08-19-2016<br>"
        f"/api/v1.0/08-19-2016/08-18-2017"
    )

# Precipitation route
#@app.route('/api/v1.0/precipitation')

# Stations route
@app.route('/api/v1.0/stations')
def stations():
    # Create session, query, and close session
    session = Session(engine)
    results = session.query(Station.station, Station.name, Station.latitude,
        Station.longitude,Station.elevation).all()
    session.close()

    # Create dictionary
    all_stations = [{'station': result[0], 'name': result[1], 'lat': result[2], 'lng': result[3], 'elev': result[4]} for result in results[:len(results)]]
    return jsonify(all_stations)
# Temperatures route
#@app.route('/api/v1.0/tobs')

# Min, max, avg route (start only)
#@app.route('/api/v1.0/<start>')

# Min, max, avg route
#@app.route('/api/v1.0/<start>/<end>')


# Code to run app

if __name__ == "__main__":
    app.run(debug = True)

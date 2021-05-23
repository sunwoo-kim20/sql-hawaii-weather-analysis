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
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Create session, query, and close session
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    # Create dictionary
    all_prcp = [{result[0] : result[1]} for result in results[:len(results)]]
    return jsonify(all_prcp)

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
@app.route('/api/v1.0/tobs')
def tobs():
    # Create session
    session = Session(engine)

    # Get most recent date and 12 months prior
    date = session.query(Measurement.date).\
    filter(Measurement.station == most_active_stn).\
    order_by(Measurement.date.desc()).\
    first()
    temp_query_date = dt.date(2017,8,18) - dt.timedelta(days = 365)

    # Query
    last_year_temps = session.query(Measurement.tobs).\
    filter(Measurement.date > temp_query_date).\
    filter(Measurement.station == most_active_stn).statement

    # Close session
    session.close()

# Min, max, avg route (start only)
#@app.route('/api/v1.0/<start>')

# Min, max, avg route
#@app.route('/api/v1.0/<start>/<end>')


# Code to run app

if __name__ == "__main__":
    app.run(debug = True)

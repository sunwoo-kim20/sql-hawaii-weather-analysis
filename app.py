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
        f"/api/v1.0/{{YYYY-MM-DD}}<br>"
        f"/api/v1.0/{{YYYY-MM-DD}}/{{YYYY-MM-DD}}"
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

    # Get most active station
    observation_counts = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).\
    all()

    most_active_stn = observation_counts[0][0]

    # Get most recent date and 12 months prior
    date = session.query(Measurement.date).\
    filter(Measurement.station == most_active_stn).\
    order_by(Measurement.date.desc()).\
    first()[0]
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    temp_query_date = dt.date(year, month, day) - dt.timedelta(days = 365)

    # Query
    results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > temp_query_date).\
    filter(Measurement.station == most_active_stn).all()

    # Close session
    session.close()

    # Create dictionary
    previous_year_temps = [{result[0]:result[1]} for result in results[:len(results)]]
    return jsonify(previous_year_temps)


# Min, max, avg route (start only)
@app.route('/api/v1.0/<start>')
def start_summary(start):

    try:
        # Create datetime object
        if len(start) != 10:
            return jsonify({"error": f"{start} is not a valid date. please try again with YYYY-MM-DD format"}), 404
        year = int(start[0:4])
        month = int(start[5:7])
        day = int(start[8:10])
        query_date = dt.date(year, month, day)
    except:
        return jsonify({"error": f"{start} is not a valid date. please try again with YYYY-MM-DD format"}), 404

    # Create session, query, and close session
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= query_date).\
    all()
    session.close()

    # Create dictionary
    summary = [{'date_start':query_date, 'min':result[0], 'max':result[1], 'avg':result[2]} for result in results[:len(results)]]

    return jsonify(summary)

# Min, max, avg route
@app.route('/api/v1.0/<start>/<end>')
def start_end_summary(start, end):

    try:
        # Create datetime object
        if len(start) != 10 or len(end) !=10:
            return jsonify({"error": f"Please try again with YYYY-MM-DD format"}), 404
        # Create start datetime object
        start_year = int(start[0:4])
        start_month = int(start[5:7])
        start_day = int(start[8:10])
        start_query_date = dt.date(start_year, start_month, start_day)

        # Create end datetime object
        end_year = int(end[0:4])
        end_month = int(end[5:7])
        end_day = int(end[8:10])
        end_query_date = dt.date(end_year, end_month, end_day)
    except:
        return jsonify({"error": f"Please try again with YYYY-MM-DD format"}), 404

    # Create session, query, and close session
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start_query_date).\
    filter(Measurement.date <= end_query_date).all()

    session.close()

    # Create dictionary
    summary = [{'date_start':start_query_date, 'date_end':end_query_date, 'min':result[0], 'max':result[1], 'avg':result[2]} for result in results[:len(results)]]
    return jsonify(summary)


# Code to run app

if __name__ == "__main__":
    app.run(debug = True)

from flask import Flask, jsonify

# Flask Setup
app = Flask(__name__)

# Home page route
@app.route('/')

# Precipitation route
@app.route('/api/v1.0/precipitation')

# Stations route
@app.route('/api/v1.0/stations')

# Temperatures route
@app.route('/api/v1.0/tobs')

# Min, max, avg route (start only)
@app.route('/api/v1.0/<start>')

# Min, max, avg route
@app.route('/api/v1.0/<start>/<end>')

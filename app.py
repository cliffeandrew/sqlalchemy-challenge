import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/Hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    """All available api routes."""
    return (
        f"Available Hawaii Weather Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"api/v1.0/<start><br/>"
        f"api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    all_results = []
    for date, prcp in results:
        results_dict = {}
        results_dict["date"] = date
        results_dict["prcp"] = prcp
        all_results.append(results_dict)

    return jsonify(all_results)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    session.close()

    all_results = []
    for station, name, latitude, longitude, elevation in results:
        results_dict = {}
        results_dict["station"] = station
        results_dict["name"] = name
        results_dict["latitude"] = latitude
        results_dict["longitude"] = longitude
        results_dict["elevation"] = elevation
        
        all_results.append(results_dict)

    return jsonify(all_results)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519397').all()
    session.close()

    all_results = []
    for station, date, tobs in results:
        results_dict = {}
        results_dict["station"] = station
        results_dict["date"] = date
        results_dict["tobs"] = tobs
        all_results.append(results_dict)

    return jsonify(all_results)


if __name__ == '__main__':
    app.run(debug=True) 

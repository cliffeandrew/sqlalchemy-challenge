import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify




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
    results = session.query(last_year_pd.date, last_year_pd.prcp).all()
    session.close()

    all_results = []
    for date, prcp in results:
        results_dict = {}
        results_dict["date"] = date
        results_dict["prcp"] = prcp
        all_results.append(results_dict)

    return jsonify(all_results)



if __name__ == '__main__':
    app.run(debug=True) 

# 1. Import Flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
​from sqlalchemy import asc, desc
from flask import Flask, jsonify
​
​
#################################################
# Database Setup
#################################################
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/project_olympics')

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)
# ​
# # Save reference to the tables
# Measurement = Base.classes.measurement
# Station = Base.classes.station
# ​
# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)
# ​
# ​
# ​
# # 3. Define static routes
# @app.route("/")
# def home():
#     return (
#         f"Welcome to the SQLAlchemy Homework - Surfs Up!<br/>"
#         f"Available Routes:<br/>"
#         f"/api/v1.0/precipitation <br/>"
#         f"/api/v1.0/stations <br/>"
#         f"/api/v1.0/tobs <br/>"
#         f"/api/v1.0/start/<start> <br/>"
#         f"/api/v1.0/start-end/<start>/<end> <br/>"
#     )
# ​
# ​
# # Precipitation Dict 
# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)
#     # Query 
#     results = session.query(Measurement.date, Measurement.prcp).all()
#     session.close()
# ​
#     #Create a dictionary, it should be date:prcp value 
#     all_data = []
#     for date, prcp in results:
#         prcp_dict = {}
#         prcp_dict[date] = prcp
# ​
#         all_data.append(prcp_dict)
# ​
#     return jsonify(all_data)
# ​
# # Stations List 
# @app.route("/api/v1.0/stations")
# def stations():
#     session = Session(engine)
#     all_stations = session.query(Station.station).all()
#     session.close()
#     return jsonify(all_stations)
# ​
# ​
# #TOBS for the most active Station "USC00519281"
# @app.route("/api/v1.0/tobs")
# def tobs():
#     session = Session(engine)
#     results = session.query(Measurement.tobs).\
#     filter(Measurement.station == "USC00519281").\
#     filter(Measurement.date > "2016-08-18").all()
#     all_tobs = list(np.ravel(results))
#     session.close()
# ​
#     return jsonify(all_tobs)
# ​
# #My tutor explained how to pass the start variable. 
# ​
# @app.route("/api/v1.0/start/<start>")
# def start_date(start):
#     session = Session(engine)
#     sel = [Measurement.date, 
#         func.avg(Measurement.tobs), 
#         func.max(Measurement.tobs), 
#         func.min(Measurement.tobs)]
#     results = session.query(*sel).\
#         filter(Measurement.date >=start).all()
        
#     session.close()
# ​
#     all_data = []
#     for x in results:
#         all_data.append({'date': x[0],'avg tobs': x[1],'max tobs': x[2],'min tobs': x[3]})
# ​
#     return jsonify(all_data)
# ​
# @app.route("/api/v1.0/start-end/<start>/<end>")
# def start_end_date(start, end):
#     session = Session(engine)
#     sel = [Measurement.date, 
#         func.avg(Measurement.tobs), 
#         func.max(Measurement.tobs), 
#         func.min(Measurement.tobs)]
#     results = session.query(*sel).\
#         filter(Measurement.date >=start).filter(Measurement.date <=end).all()
        
#     session.close()
# ​
#     all_data = []
#     for x in results:
#         all_data.append({'date': x[0],'avg tobs': x[1],'max tobs': x[2],'min tobs': x[3]})
# ​
#     return jsonify(all_data)
# ​
 if __name__ == "__main__":
     app.run(debug=True)
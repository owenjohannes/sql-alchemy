import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify

#setting up the database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
connect = engine.connect()

base = automap_base()
base.prepare(engine, reflect = True)

#classes
base.classes.keys()

# Save references to each table
analysis = base.classes.measurement
station = base.classes.station
session = Session(engine)

#setting up flask
app = Flask(__name__)

#setting up flask routes
@app.route("/")

def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>(yyyy-mm-dd)<br/>"
        f"/api/v1.0/<start>(yyyy-mm-dd/<end>yyyy-mm-dd)<br/>"
    )

@app.route('/api/v1.0/<start>')
def start(start):
    session = Session(engine)
    queryresult = session.query(func.min(analysis.tobs), func.avg(analysis.tobs), func.max(analysis.tobs)).\
        filter(analysis.date >= start).all()
    session.close()

    tobsall = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

@app.route('/api/v1.0/<start>/<end>')
def start_end(start,end):
    session = Session(engine)
    queryresult = session.query(func.min(analysis.tobs), func.avg(analysis.tobs), func.max(analysis.tobs)).\
        filter(analysis.date >= start).filter(analysis.date <= end).all()
    session.close()

    tobsall = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    lateststr = session.query(analysis.date).filter(analysis.station == "USC00519281").order_by(analysis.date.desc()).first()[0]
    latestdate = dt.datetime.strptime(lateststr, '%Y-%m-%d')
    querydate = dt.date(latestdate.year -1, latestdate.month, latestdate.day)
    sel = [analysis.date,analysis.tobs]
    queryresult = session.query(*sel).filter(analysis.date >= querydate).all()
    session.close()

    tobsall = []
    for date, tobs in queryresult:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tobsall.append(tobs_dict)


@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    sel = [station.station]
    queryresult = session.query(*sel).all()
    session.close()

    stations_list = []
    for row in queryresult:
        station_dict = {}
        station_dict["station"] = row[0]
        stations_list.append(station_dict)

    return jsonify(stations_list)



@app.route("/api/v1.0/precipitation")

def precipitation():
    session = Session(engine)
    sel = [analysis.date,analysis.prcp]
    queryresult = session.query(*sel).all()
    session.close()

    precipitation = []
    for date, prcp in queryresult:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)

if __name__ == "__main__":
    app.run(debug=True)
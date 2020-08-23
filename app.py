# Import Flask and other dependencies
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from scipy import stats
from numpy import mean
from flask import Flask, jsonify
#from flask import request, redirect

#Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# save references to files
Measurement = Base.classes.measurement
Station = Base.classes.station

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    print("")
    return (
        f"Welcome to the Vacation API!<br/>"
        f"<br>"
        f"We have Waihee HI weather for 2016-08-24 through 2017-08-23.<br/>"
        f"For other information, try Google.<br/>"
        f"<br>"
        f"Available Routes:<br/>"
        f"Precipitation data: /api/v1.0/precipitation<br/>"    
        f"Station information: /api/v1.0/stations<br/>"           
        f"Temperature data: /api/v1.0/temperature<br/>"
        f"<br>"
        f"For min, mean, and max temperatures from a given date forward, use address below with date as YYYY-MM-DD<br/>"
        f"/api/v1.0/start_from/<start1><br/>"
        f"<br>"
        f"For min, mean, and max temperatures between two dates, use address below with dates as YYYY-MM-DD,YYYY-MM-DD<br/>"
        f"/api/v1.0/between/<start2><end><br/>"
        f"<br>"
        f"To be asked for start and end dates in the terminal, use address below.<br/>"
        f"/api/v1.0/between/with_input<br/>"
        f"<br>"
        f"Want to be asked for start and end dates in a form? Too bad, too much work...<br/>"
#        f"/api/v1.0/get_dates"

   )

# 4. Define what to do when a user hits the other routes
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("")
    session = Session(engine)
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_day_last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    station_tobs_activity =  session.query(Measurement.station, func.count(Measurement.tobs)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.tobs).desc()).\
    all()
    busiest_station = station_tobs_activity[0][0]
    busiest_station_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > last_day_last_year).\
        filter(Measurement.station==busiest_station).all() 
    busiest_station_prcp_dict = dict(busiest_station_prcp)
    return jsonify(busiest_station_prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    print("")
    session = Session(engine)
    station_information = session.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, \
        Station.elevation).all() 
    station_information_df = pd.DataFrame(station_information, columns=['id', 'station', 'name', 'latitude', 'longitude', 'elevation'])
    station_information_dict = station_information_df.to_dict('records')
    #One alternative version:
    #station_information_dict = station_information_df.to_dict()
    return jsonify(station_information_dict)

@app.route("/api/v1.0/temperature")
def temperature():
    print("")
    session = Session(engine)
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_day_last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    station_tobs_activity =  session.query(Measurement.station, func.count(Measurement.tobs)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.tobs).desc()).\
    all()
    busiest_station = station_tobs_activity[0][0]
    busiest_station_tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > last_day_last_year).\
        filter(Measurement.station==busiest_station).all() 
    busiest_station_tobs_dict = dict(busiest_station_tobs)
    return jsonify(busiest_station_tobs_dict)    

@app.route("/api/v1.0/start_from/<start1>")
def weather_from_start_date(start1):
    session = Session(engine)   
    station_tobs_activity =  session.query(Measurement.station, func.count(Measurement.tobs)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.tobs).desc()).\
    all()
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    busiest_station = station_tobs_activity[0][0]  
    tobs_stats_from_start_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
              func.max(Measurement.tobs)).filter(Measurement.station == busiest_station).filter(Measurement.date >= start1).all()
    tobs_min_from_start_date = session.query(func.min(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start1).all()  
    tobs_avg_from_start_date = session.query(func.avg(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start1).all()  
    tobs_max_from_start_date = session.query(func.max(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start1).all()  
    return f'The minimum temperature (˚F) between {start1} and {last_day} was {tobs_min_from_start_date}; \
        the mean was {tobs_avg_from_start_date}; and the maximum was {tobs_max_from_start_date}.'  
    
@app.route("/api/v1.0/between/<start2>,<end>")
def weather_from_start_to_finish_date(start2, end1):
    print("")
    session = Session(engine)   
    station_tobs_activity =  session.query(Measurement.station, func.count(Measurement.tobs)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.tobs).desc()).\
    all()   
    busiest_station = station_tobs_activity[0][0] 
    tobs_min_for_interval = session.query(func.min(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start2).filter(Measurement.date <= end1).all()  
    tobs_avg_for_interval = session.query(func.avg(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start2).filter(Measurement.date <= end1).all()  
    tobs_max_for_interval = session.query(func.max(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start2).filter(Measurement.date <= end1).all()  
    return f'The minimum temperature (˚F) between {start2} and {end1} was {tobs_min_for_interval}; \
        the mean was {tobs_avg_for_interval}; and the maximum was {tobs_max_for_interval}.'  

@app.route("/api/v1.0/between/with_input")
def weather_from_start_to_finish_with_input():
    print("")
    session = Session(engine)   
    station_tobs_activity =  session.query(Measurement.station, func.count(Measurement.tobs)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.tobs).desc()).\
    all()   
    date_entry = input('Enter a start date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))
    start3 = dt.date(year, month, day)
    date_entry = input('Enter an end date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))
    end2 = dt.date(year, month, day)
    busiest_station = station_tobs_activity[0][0] 
    tobs_min_for_input_interval = session.query(func.min(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start3).filter(Measurement.date <= end2).all()  
    tobs_avg_for_input_interval = session.query(func.avg(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start3).filter(Measurement.date <= end2).all()  
    tobs_max_for_input_interval = session.query(func.max(Measurement.tobs)).filter(Measurement.station == busiest_station).\
        filter(Measurement.date >= start3).filter(Measurement.date <= end2).all()  
    return f'The minimum temperature (˚F) between {start3} and {end2} was {tobs_min_for_input_interval}; \
        the mean was {tobs_avg_for_input_interval}; and the maximum was {tobs_max_for_input_interval}.'  
 


if __name__ == "__main__":
    app.run(debug=True)

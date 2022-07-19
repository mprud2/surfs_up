# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Build SQLAlchemy engine for database querying
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database into classes (Capitalize 'Base' to reflect that it is a class)
Base = automap_base()
Base.prepare(engine, reflect=True)

# # If this were a Jupyter Notebook, you would view Classes to help with creating variables for each class
# class_keys = Base.classes.key()

# Assign variables to each class
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Create an instance of Flask, with an application called 'app'
app = Flask(__name__)

# # Create an instance of Flask
# app = Flask(__name__)

# # Create Flask root
@app.route("/")

# Create a function with return statements that generate the other routes using f-strings
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br/>
    Available Routes: <br/>
    /api/v1.0/precipitation <br/>
    /api/v1.0/stations <br/>
    /api/v1.0/tobs <br/>
    /api/v1.0/temp/start/end <br/>
    ''')

# Build 'precipation' route
@app.route("/api/v1.0/precipitation")

# Create 'precipitation' function.  
    # Add a line of code that calculates the query dates
        # Write a query to get the date and precipitation for the previous year
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    # Create a dictionary out of queried data
    precip = {date: prcp for date, prcp in precipitation}
    # Convert dictionary into a JSON file
    return jsonify(precip)

# Build 'stations' route
@app.route("/api/v1.0/stations")

# Create 'stations' function.  
    # Add a line of code that returns all of the stations in our database
        # start by unraveling our results into a one-dimensional array. 
        # To do this, we want to use the function np.ravel(), with 'results' as our parameter
        # convert our unraveled results into a list by using the list() function, 
        # and then convert that array into a list. Then we'll jsonify the list and return it as JSON
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Build 'Observed Temperatures' route
@app.route("/api/v1.0/tobs")

# Create a monthly temperatures function
    # create a variable for the last year's dates
    # query the primary station for all the temperature observations from the previous year
    # convert our unraveled results into a list by using the list() function, 
    # and then convert that array into a list. Then we'll jsonify the list and return it as JSON
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Build a statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create 'stats' function
    #create a query to select the minimum, average, and maximum temperatures from our SQLite database
    # we need to determine the starting and ending date, add an if-not statement to our code. 
    # query our database using the list that we just made. 
    # unravel the results into a one-dimensional array and convert them to a list. 
    # jsonify our results and return them.
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
        
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
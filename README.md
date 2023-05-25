#sql-alchemy
This repository contains code and files for analyzing climate data and creating a Flask API based on the analysis. The analysis is performed using Python, SQLAlchemy, Pandas, and Matplotlib.

##Files      
climate_starter.ipynb: Jupyter Notebook containing the climate data analysis and exploration code.      
hawaii.sqlite: SQLite database file containing the climate data.      
app.py: Flask application code for the API.      
README.md: Readme file explaining the repository.

##Climate Data Analysis       
The climate_starter.ipynb notebook performs the following tasks:        
1. Connects to the SQLite database using SQLAlchemy.        
2. Reflects the tables in the database and saves references to the station and measurement classes.
3. Performs a precipitation analysis:
- Finds the most recent date in the dataset.
- Retrieves the previous 12 months of precipitation data.
- Loads the query results into a Pandas DataFrame and sorts them by date.
- Plots the precipitation data using Matplotlib.
- Prints the summary statistics for the precipitation data.
4. Performs a station analysis:
- Calculates the total number of stations in the dataset.
- Finds the most active station based on the observation counts.
- Calculates the lowest, highest, and average temperatures for the most active station.
- Retrieves the previous 12 months of temperature observation data for the most active station.
- Plots a histogram of the temperature observations using Matplotlib.

##Flask API
The Flask API is implemented in the app.py file. It provides the following routes:
- /: Homepage that lists all the available routes.
- /api/v1.0/precipitation: Returns the precipitation data as a JSON dictionary with date as the key and precipitation as the value.
- /api/v1.0/stations: Returns a JSON list of stations from the dataset.
- /api/v1.0/tobs: Returns a JSON list of temperature observations for the most active station for the previous year.
- /api/v1.0/<start>: Returns a JSON list of the minimum, average, and maximum temperatures calculated from the specified start date to the end of the dataset.
- /api/v1.0/<start>/<end>: Returns a JSON list of the minimum, average, and maximum temperatures calculated from the specified start date to the specified end date.
The API connects to the SQLite database, uses SQLAlchemy to query the data, and returns the results as JSON responses.







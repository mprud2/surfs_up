# surfs_up
Module 9 work with SQLite, SQL Alchemy, and Flask

## Overview of the Analysis

The purpose of this project is to investigate the weather patterns on the island of Oahu to determine whether it is conducive to opening an ice cream and surf shop on the island, named Surf n' Shake.  One of the potential investors asked us to investigate a dataset of temperature and precipitation measurements from nine different weather stations on the island of Oahu.  Some of the primary concerns from this investor were whether it would rain too much or if the temperatures would not be favorable year-round.  

In order to conduct this analysis, we used SQLite to explore the data, SQLAlchemy to reflect the data into tables that we could query, Jupyter Notebook to create the code, and Flask to create a webpage where other potential investors can see the results.

### Data Sources and Tools Used
- Data Source: hawaii.sqlite
- Tools Used: Python SQL toolkit (SQLAlchemy), Object Relational Mapper, pandas, numpy
- Software: SQLlite, Python 3.7.13, Flask, Jupyter Notebook
- Deliverables: SurfsUp_Challenge.ipynb, climate_analysis.ipynb

## Results
An initial exploration of the weather data was undertaken to determine the precipitation for each day for the previous year.  A plot (Figure 1) was made of the precipitation by day from the nine weather stations on Oahu (listed in Figure 2).  It showed that there were only four days when rain surpassed 4 inches in a given day.  Half of the days received less than .02 inches of rain a day.  There also seemed to be a higher average amount of rain per day in the late summer and early spring timeframes.  The overall low amounts of precipitation seem to be a good indicator that business will not be hampered by rain.  The data (Figure 3) also shows that of the 2,021 data points gathered by the 9 stations, over a quarter of the data measured no rain at all.  This also seems to be a good indicator of favorable weather for surfing.
![YearofPrecipitation_BarChart](https://user-images.githubusercontent.com/104801614/179864632-6b1a037b-c3da-4c35-9814-8bd21d651b2d.png)
##### Figure 1: Bar chart displaying the amount of precipitation in inches for each day, as measured by 9 weather stations on Oahu.
![WeatherStations_andMeasurements](https://user-images.githubusercontent.com/104801614/179864603-0d21373e-135b-4086-b55e-622cd5b51ebd.png)
##### Figure 2: List of the weather stations that were included in the analysis, with number of measurements reported from each station.
![Precipitation_describe_results](https://user-images.githubusercontent.com/104801614/179864621-21dab0c6-1ea2-43f6-9fa1-cd7a1741e7b9.png)
##### Figure 3: Measures of central tendency for precipitation from August 2016 to August 2017 on Oaho

Precipitation was not the only variable that was identified that could affect business.  Therefore, a histogram of temperatures measured at the most active weather station (USC00519281) was created (Figure 4)
![TemperatureFrequencyHistogram](https://user-images.githubusercontent.com/104801614/179866669-929b8f0d-3d35-4fc0-9280-2b7fd9484f3d.png)
##### Figure 4: Histogram of temperature readings from Weather Station USC00519281
## Summary

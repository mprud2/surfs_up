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

Precipitation was not the only variable that was identified that could affect business.  Therefore, a histogram of temperatures measured at the most active weather station (USC00519281) was created (Figure 4).  From it, we can see that the the temperature is most commonly between 70-80 degrees Farenheit.  This would also seem to be a good temperature range for a Surf n' Shake, as it is not too cold to ice cream consumption, but not too hot to deter surfers. Furthermore, summary statistics for temperature readings in June (Figure 5) and December (Figure 6) were made for the time period of 2010 to 2017.  While the temperatures are generally cooler in December than June (71° vs. 74°), the tropical climate of Hawaii should still allow for surfing year round.

![TemperatureFrequencyHistogram](https://user-images.githubusercontent.com/104801614/179866669-929b8f0d-3d35-4fc0-9280-2b7fd9484f3d.png)
##### Figure 4: Histogram of temperature readings from Weather Station USC00519281
![JuneTemperatureSummaryStatistics](https://user-images.githubusercontent.com/104801614/179867093-976fc02f-6fdd-42a8-bb7f-13fd0f715ef2.png)
##### Figure 5: Summary Statistics for temperature readings in June from 2010-2017
![DecemberTemperatureSummaryStatistics](https://user-images.githubusercontent.com/104801614/179867101-f8d987b3-a07c-4e4f-8015-c58677f2bd88.png)
##### Figure 6: Summary Statistics for temperature readings in December from 2010-2017

## Summary
The weather data analyzed for the island of Oahu appears to show that the climate would be accommodating to a business such as Surf n' Shake.  The temperature ranges are consistent year round, and rain is not overwhelming.  I would recommend that further queries could be made to further explore this financial decision, however. For instance, we only looked at one year of precipitation data.  If 2017 was an anomalous year, it may not give a good impression of the overall climate.  More years could easily be added to the analysis.  Likewise, the temperature histogram was made for only one of the weather stations.  It is possible that one side of the island could have more rain or higher temperatures than the other side of the island, and that might provide more information to optimize the location of the actual store.  Finally, the weather stations also have latitude, longitude, and elevation data that could be used to create visualizations using APIs to display their locations and see if any interesting observations could be made that might affect a final decision. 

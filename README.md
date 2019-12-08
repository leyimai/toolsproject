This is Squirrel Tracker 1.0
====================================


What is it?
-------------------
Squirrel tracker is a web application developed with Django Framework for users to keep track of all the spotted squirrels in NYC. On the app, Users are allowed to add, update, and view squirrel data. The current dataset includes the 2018 Central Park Squirrel Census data，which can be downloaded at NYCOpenData. 

- Website: https://splendid-window-255500.appspot.com/sightings/
- Data Source: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data


Main Features
-------------------
Squirrel Tracker app includes two sub-apps with the following features:

Sightings: a site that lists all squirrels, with links to edit each squirrel based on unique squirrel ID or add new squirrels.

    - /sightings/add
    - /sightings/<unique_squirrel_id>
    - /sightings/stats
    
Map: an interactive map that visualizes the reported squirrels' locations. The map application was built with Leaflet and OpenStreetMaps.See documentation of Leaflet at https://leafletjs.com/reference-1.6.0.html.
    
    - /map


How to run on server?
------------------
The link to the server running your application

    https://splendid-window-255500.appspot.com/sightings/


Contributors
-----------------------
- Yuemeng Zhang (uni: yz3684)
- Leyi Mai (uni: lm3504)

From Group 65, Tools for Analytics(Sec 2)


Dependencies
------------
It is necessary to install Django 2.2.7.

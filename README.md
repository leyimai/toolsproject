This is Squirrel Tracker 1.0
====================================


What is it?
-------------------
Squirrel tracker is a web application developed with Django Framework for users to keep track of all the spotted squirrels in Central Park, NYC. On the app, Users are allowed to add, update, and view squirrel sightings. The current dataset includes the 2018 Central Park Squirrel Census data，which can be downloaded at NYCOpenData https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data.


How to run the application?
-----------------------------

Click the following link to the server to run the web application:

    - https://splendid-window-255500.appspot.com/sightings


Main Features
-------------------
Squirrel Tracker app includes two sub-apps with the following features:

Sightings (Main Page): a site that lists all squirrels, with links to edit or add squirrels, view squirrel statistics and the map. This site uses Bootstrap4 for styling (reference at https://getbootstrap.com/docs/4.0/getting-started/introduction/).

    - https://splendid-window-255500.appspot.com/sightings

Following are the links to add a squirrel sighting, update an existing sighting and view sighting statistics, respectively.

    - https://splendid-window-255500.appspot.com/sightings/add
    - https://splendid-window-255500.appspot.com/sightings/<unique_squirrel_id>
    - https://splendid-window-255500.appspot.com/sightings/stats
    
Map: an interactive map that visualizes the reported squirrels' locations. The map application was built with Leaflet and OpenStreetMaps. See documentation of Leaflet at https://leafletjs.com/reference-1.6.0.html.
    
    - https://splendid-window-255500.appspot.com/map


Contributors
-----------------------
- Yuemeng Zhang (uni: yz3684)
- Leyi Mai (uni: lm3504)

From Group 65, Tools for Analytics(Sec 2)


Dependencies
------------
It is necessary to install Django 2.2.7.

## PyQuake-cli: Stay Updated on Earthquakes in the Terminal

**Welcome to PyQuake-cli!** This Python application brings the latest earthquake information straight to your terminal.

**How it works:**

- PyQuake fetches data from the USGS hourly earthquake feed.
- It parses the JSON data and displays detailed information about each earthquake, including:
    - URL
    - Magnitude
    - Location

**Features:**

- Live feed of recent earthquakes
- Detailed earthquake information
- Summary of recent earthquakes, showing magnitude and location
- Simple and user-friendly terminal interface

**Getting started:**

1. Install PyQuake: `pip install requests json sys && git clone https://github.com/WalkTheEarth/PyQuake.git`
2. Run the application: `python3 PyQuake.py`
   
   ![regular mode on PyQuake](https://raw.githubusercontent.com/WalkTheEarth/PyQuake-cli/main/img/NoSimple.png)
   
4. For a summary of recent earthquakes: `python3 PyQuake.py /s`
   
   ![Simple Mode on PyQuake](https://raw.githubusercontent.com/WalkTheEarth/PyQuake-cli/main/img/Simple.png)
   

**Future plans:**

- Filter earthquakes by location/magnitude
- Add interactive map visualization
- Allow saving earthquakes to a file/database

**Get alerted about earthquakes in real-time with PyQuake-cli!**

## More Information

- **Data source:** USGS Earthquake Feed
- **Dependencies:** requests, json, sys
- **License:** AGPL-3.0

**Join the discussion and contribute ideas for future features!**

## Thank you for using PyQuake-cli!

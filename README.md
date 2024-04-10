# PyQuake-cli
A python application that uses the USGS hourly feed and displays it in terminal


Installation


To install PyQuake do the following.

` (sudo) pip install requests json sys `

then

` git clone https://www.github.com/WalkTheEarth/PyQuake.git `

next, if everything worked, do

`python3 (just python on windows) PyQuake.py`

if everything worked, it should be something like 

` URL: https://earthquake.usgs.gov/earthquakes/eventpage/ak0244naie2j
Magnitude: 0.9
Location: 67 km WNW of Tyonek, Alaska`

`URL: https://earthquake.usgs.gov/earthquakes/eventpage/ak0244nafbjp
Magnitude: 5
Location: 66 km W of Patacamaya, Bolivia`

`URL: https://earthquake.usgs.gov/earthquakes/eventpage/us7000mb79
Magnitude: 1.9
Location: 27 km NW of Nikiski, Alaska`

`URL: https://earthquake.usgs.gov/earthquakes/eventpage/ak0244naavwy
Magnitude: 3.26
Location: 75 km NNE of Luquillo, Puerto Rico`

`URL: https://earthquake.usgs.gov/earthquakes/eventpage/pr71445328
Magnitude: 5.4
Location: 40 km NW of Kuqa, China `

if your looking for something more simpler, run the same command from earlier, but add "/s" at the end so it becomes

`python3 (just python on windows) PyQuake.py /s`

and it should return 

`Earthquakes Summary:`

`M 1.0 - 9 km E of Pala, CA`

`M 1.3 - 7 km S of Houston, Alaska`

`M 0.9 - 67 km WNW of Tyonek, Alaska`

`M 5.0 - 66 km W of Patacamaya, Bolivia`

`M 1.9 - 27 km NW of Nikiski, Alaska`

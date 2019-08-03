# pyNav
Flight planner for VFR flights

Adrien Crovato, 2019

[![Apache License Version 2.0](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)

## Features
Python toolset computing and tracing a VFR navigation route.
* Simple to use and cross platform
* Create a flight log and export the route to gpx format

## Usage
Get the code with git
```
git clone https://github.com/acrovato/pyNav.git
```
Create your navigation input file and compute the route
```
cd pyNav
python run.py /path/to/nav.py
```
A workspace folder will be created and will contain two files:
  - a log file in text format,
  - a gpx file than can be vizualized from the web (e.g. https://www.gpsvisualizer.com/).

Sample navigation input files can be found under the [tests](/tests) folder.
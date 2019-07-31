#! /usr/bin/env python
# -*- coding: utf-8; -*-

'''
Template short navigation
Adrien Crovato
2019
'''

def params():
    ''' Set of parameters
    '''
    p = {}
    # set steerpoints as list
    p['Steerpoints'] = [ ['EBLG', '5038N', '00527E'], 
                         ['EBLG-ECHO', '5041N', '00539E'],
                         ['EBSP', '5029N', '00555E'] ]
    # set flight parameters
    p['CAS'] = 85 # calibrated airspeed [kts]
    p['FuelFlow'] = 5.2 # fuel consumption [USG/h]
    # set atmospheric parameters
    p['Wind'] = [250, 15] # wind direction [deg] and speed [kts]
    p['OAT'] = 20 # outside air temperature at considered altitude [C]
    p['Altitude'] = [2000, 2000] # pressure altitude [feet]
    return p

def main():
    ''' Execute
    '''
    import os.path
    import planner as pln
    plan = pln.Planner(params())
    plan.log(os.path.splitext(os.path.basename(__file__))[0]+'.log')
    plan.gpx(os.path.splitext(os.path.basename(__file__))[0]+'.gpx')

if __name__ == "__main__":
    main()
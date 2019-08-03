#! /usr/bin/env python
# -*- coding: utf-8; -*-

'''
Template long navigation
Adrien Crovato
2019
'''

def params():
    ''' Set of parameters
    '''
    p = {}
    # set steerpoints as list
    p['Steerpoints'] = [ ['EBLG', '5038N', '00527E'], 
                         ['EBLG-ROMEO', '5042N', '00518E'],
                         ['FLORA', '5053N', '00509E'],
                         ['EBAW-LIERA', '5107N', '00437E'],
                         ['Crossings', '5059N', '00350E'],
                         ['EBOS-ALTER', '5105N', '00327E'],
                         ['EBOS-BOSSY', '5112N', '00304E'],
                         ['EBOS', '5113N', '00252E'],
                         ['EBOS-GESPO', '5109N', '00256E'],
                         ['EBOS-TURUT', '5104N', '00306E'],
                         ['EBCI-WATERLOO', '5041N', '00424E'],
                         ['Gembloux', '5034N', '00442E'],
                         ['EBNM', '5029N', '00446E'],
                         ['EBLG-WISKY', '5035N', '00513E'],
                         ['EBLG', '5038N', '00527E'] ]
    # set flight parameters
    p['CAS'] = 85 # calibrated airspeed [kts]
    p['FuelFlow'] = 5.2 # fuel consumption [USG/h]
    # set atmospheric parameters
    p['Wind'] = [360, 5] # mean wind direction [deg] and speed [kts]
    p['OAT'] = [15, 15, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 15, 15] # list of outside air temperature at considered altitude [C]
    p['Altitude'] = [2000, 2000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 2000, 2000] # list of pressure altitude [feet]
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
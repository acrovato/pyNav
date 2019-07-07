#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Flight planner
Adrien Crovato
2019
'''

class Planner:
    def __init__(self, p):
        ''' Fill flight plan
        '''
        import steerpoint as sp
        import leg
        # create
        self.strp = []
        self.legs = []
        for i in range(0, len(p['Steerpoints'])):
            self.strp.append(sp.Steerpoint(i, p['Steerpoints'][i][0], p['Steerpoints'][i][1], p['Steerpoints'][i][2]))
        for i in range(0, len(p['Steerpoints']) - 1):
            self.legs.append(leg.Leg(i, self.strp[i], self.strp[i+1], p['CAS'], p['Altitude'], p['OAT'], p['Wind'], p['FuelFlow']))
    
    def log(self, fname):
        ''' Create log
        '''
        f = open(fname, 'w')
        f.write('{0:>12s}   {1:>12s}   {2:>12s}   {3:>12s}   {4:>12s}   {5:>12s}   {6:>12s}   {7:>12s}   {8:>12s}   {9:>12s}\n'.format('Steerpoint', 'Coordinates', 'Track', 'Altitude', 'TAS', 'Heading', 'Distance', 'GS', 'Time', 'Fuel'))
        for i in range(0, len(self.strp)):
            f.write('{0:>12s}  ({1:>5s}{2:>6s})   \n'.format(self.strp[i].name, self.strp[i].lat, self.strp[i].lng))
            if i != len(self.strp)-1:
                f.write('{0:>12s}   {0:>12s}   {1:12.0f}   {2:12.0f}   {3:12.0f}   {4:12.0f}   {5:12.0f}   {6:12.0f}   {7:12.2f}   {8:12.1f}\n'.format('', self.legs[i].trck, self.legs[i].alt, self.legs[i].tas, self.legs[i].hdg, self.legs[i].dst, self.legs[i].gs, self.legs[i].time, self.legs[i].fuel))
        f.close()
    
    def disp(self):
        ''' Display plan
        '''
        return
    
    def export(self):
        ''' Export to gpx
        '''
        return

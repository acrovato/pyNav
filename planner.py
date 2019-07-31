#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Flight planner
Manage ations
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
        print 'Creating steerpoints...',
        for i in range(0, len(p['Steerpoints'])):
            self.strp.append(sp.Steerpoint(i, p['Steerpoints'][i][0], p['Steerpoints'][i][1], p['Steerpoints'][i][2]))
        print 'done!'
        print 'Creating legs... ',
        for i in range(0, len(p['Steerpoints']) - 1):
            self.legs.append(leg.Leg(i, self.strp[i], self.strp[i+1], p['CAS'], p['Altitude'][i], p['OAT'], p['Wind'], p['FuelFlow']))
        print 'done!'
        # compute total
        self.total()

    def total(self):
        '''Compute flight distance, time and fuel
        '''
        import math
        # compute total
        self.fdist = 0
        self.ftime = 0
        self.ffuel = 0
        for i in range(0, len(self.legs)):
            self.fdist += self.legs[i].dst
            self.ftime += self.legs[i].time
            self.ffuel += self.legs[i].fuel
        # convert time
        h = int(math.floor(self.ftime))
        dec = (self.ftime - h) * 60
        m = int(math.floor(dec))
        s = int(math.ceil((dec - m) * 60))
        self.ftimec = '{0:>2s}:{1:>2s}:{2:>2s}'.format(str(h), str(m), str(s))
    
    def log(self, fname):
        ''' Create log
        '''
        print 'Printing ', fname, '...',
        f = open(fname, 'w')
        f.write('{0:>16s}   {1:>12s}   {2:>12s}   {3:>12s}   {4:>12s}   {5:>12s}   {6:>12s}   {7:>12s}   {8:>12s}   {9:>12s}\n'.format('Steerpoint', 'Coordinates', 'Track', 'Altitude', 'TAS', 'Heading', 'Distance', 'GS', 'Time', 'Fuel'))
        for i in range(0, len(self.strp)):
            f.write('{0:>16s}    {1:>5s}{2:>6s}   \n'.format(self.strp[i].name, self.strp[i].lat, self.strp[i].lng))
            if i != len(self.strp)-1:
                f.write('{0:>16s}   {0:>12s}   {1:12.0f}   {2:12.0f}   {3:12.0f}   {4:12.0f}   {5:12.0f}   {6:12.0f}   {7:>12s}   {8:12.1f}\n'.format('', self.legs[i].trck, self.legs[i].alt, self.legs[i].tas, self.legs[i].hdg, self.legs[i].dst, self.legs[i].gs, self.legs[i].timec, self.legs[i].fuel))
        
        f.write('\n{0:>16s}   {1:>12s}   {1:>12s}   {1:>12s}   {1:>12s}   {1:>12s}   {2:12.0f}   {1:>12s}   {3:>12s}   {4:12.1f}\n'.format('**** TOTAL ****', '', self.fdist, self.ftimec, self.ffuel))
        f.close()
        print 'done!'
    
    def gpx(self, fname):
        ''' Export to gpx
        '''
        from datetime import datetime
        print 'Printing ', fname, '...',
        f = open(fname, 'w')
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        f.write('<gpx  version="1.1"  creator="pyNav"  xmlns="http://www.topografix.com/GPX/1/1">\n')
        f.write('  <metadata>\n')
        f.write('    <name>{0:>s}</name>\n'.format(fname[:-4]))
        f.write('    <time>{0}Z</time>\n'.format(datetime.utcnow()))
        f.write('  </metadata>\n')
        f.write('  <rte>\n')
        for i in range(0, len(self.strp)):
            f.write('  <rtept lat="{0:f}" lon="{1:f}">\n'.format(self.strp[i].latc,self.strp[i].lngc))
            f.write('    <name>{0:>s}</name>\n'.format(self.strp[i].name))
            f.write('  </rtept>\n')
        f.write('  </rte>\n')
        f.write('</gpx>\n')
        print 'done!'

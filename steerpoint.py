#! /usr/bin/env python
# -*- coding: utf-8; -*-

'''
Steerpoint
Adrien Crovato
2019
'''

class Steerpoint:
    def __init__(self, _no, _name, _lat, _lng):
        # read
        self.no = _no       # number
        self.name = _name   # name
        self.lat = _lat     # latitude DDMM[N/S]
        self.lng = _lng     # longitude DDMM[E/W]
        # convert coordinates
        self.convert()
        
    def convert(self):
        ''' Convert from DDMM to DD
        '''
        # latitude
        if len(self.lat) != 5:
            raise RuntimeError('Latitude coordinates must be entered as DDMM[N/S] string')
        self.latc = float(self.lat[0:2]) + float(self.lat[2:4])/60
        if self.lat[4] == 'S':
            self.latc = -self.latc
        # longitude
        if len(self.lng) != 6:
            raise RuntimeError('Longitude coordinates must be entered as DDDMM[E/W] string')
        self.lngc = float(self.lng[0:3]) + float(self.lng[3:5])/60
        if self.lng[5] == 'W':
            self.lngc = -self.lngc

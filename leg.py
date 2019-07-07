#! /usr/bin/env python
# -*- coding: utf-8; -*-

'''
Leg
Adrien Crovato
2019
'''

class Leg:
    def __init__(self, _no, _sps, _spe, _cas, _alt, _oat, _wnd, _flo):
        # read
        self.no = _no       # leg number
        self.sps = _sps     # initial steerpoint
        self.spe = _spe     # final steerpoint
        self.cas = _cas     # calibrated airspeed
        self.alt = _alt     # pressure altitude
        self.oat = _oat     # outside air temperature
        self.wnd = _wnd     # wind direction and speed 
        self.flo = _flo     # fuel flow
        # compute
        self.trace()
        self.speed()
        self.compute()
    
    def trace(self):
        ''' Compute leg track assuming it is rhumb line (loxodrome)
        (https://www.movable-type.co.uk/scripts/latlong.html)
        '''
        import math
        # store coordinates and convert to radians (clarity)
        phi = [math.radians(self.sps.latc), math.radians(self.spe.latc)] # latitude
        lambd = [math.radians(self.sps.lngc), math.radians(self.spe.lngc)] # longitude
        dPhi = phi[1] - phi[0]
        dLambd = lambd[1] - lambd[0]
        # projected latitude difference
        dPsi = math.log(math.tan(math.pi/4 + phi[1]/2) / math.tan(math.pi/4 + phi[0]/2))
        # corrections
        if dPsi > 1e-12:
            q = dPhi / dPsi # general formula
        else:
            q = math.cos(phi[0]) # E-W track
        if abs(dLambd) > math.pi:
            if (dLambd) > 0:
                dLambd = -2*math.pi + dLambd
            else:
                dLambd = 2*math.pi + dLambd
        # distance
        self.dst = math.sqrt(dPhi*dPhi + q*q*dLambd*dLambd) * 6371 / 1.852 # nm
        # track
        self.trck = math.degrees(math.atan2(dLambd, dPsi))
    
    def speed(self):
        ''' Convert CAS to TAS
        (https://en.wikipedia.org/wiki/Density_altitude)
        (https://www.pprune.org/questions/333787-ias-tas-formula.html)
        '''
        # density altitude
        da = self.alt + 118.8 * (self.oat - 15 + self.alt/500)
        # true airspeed
        self.tas = self.cas / (1 - 6.8755856*10**-6 * da)**2.127940
    
    def compute(self):
        ''' Compute leg heading
        (https://www.raeng.org.uk/publications/other/1-aircraft-navigation)
        '''
        import math
        # get ground speed using cosine rule: tas² = wnd² + gs² - 2*gs*wnd*cos(angle)
        wnd2 = (self.wnd[0] + 180) % 360 # wing heading
        angle = math.radians(abs(self.trck - wnd2)) # angle between track and wind
        b = -2*self.wnd[1]*math.cos(angle)
        c = self.wnd[1] * self.wnd[1] - self.tas * self.tas
        # ground speed
        self.gs = 0.5 * (-b + math.sqrt(b*b - 4*c))
        # get aircraft and (opposite) wind speed components
        vx = self.gs * math.cos(math.radians(self.trck))
        vy = self.gs * math.sin(math.radians(self.trck))
        wx = self.wnd[1] * math.cos(math.radians(self.wnd[0]))
        wy = self.wnd[1] * math.sin(math.radians(self.wnd[0]))
        # heading
        self.hdg = math.degrees(math.atan2(vy+wy,vx+wx))
        if self.hdg < 0:
            self.hdg += 360 # to get hdg in [0,360]
        # time and 3 minutes-tick distance
        self.time = self.dst / self.gs
        self.tick = 3. * self.gs
        # fuel consumption
        self.fuel = self.flo * self.time
    
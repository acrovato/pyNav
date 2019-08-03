#!/usr/bin/env python
# -*- coding: utf8 -*-
# test encoding: à-é-è-ô-ï-€
#
# run script for pyNav

def createWdir():
    import os
    wdir = os.path.join(os.getcwd(), 'workspace')
    if not os.path.isdir(wdir):
        print "creating", wdir
        os.makedirs(wdir)
    os.chdir(wdir)

def parseargs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='*', help='python file')
    return parser.parse_args()

if __name__ == "__main__":
    import sys, os
    # adds "." to the pythonpath
    thisdir = os.path.split(__file__)[0]
    sys.path.append(thisdir)
    # parse arguments
    args = parseargs()

    # get test
    testname = os.path.abspath(args.file[0])
    if not os.path.isfile(testname):
        raise Exception("file not found: %s" % testname)
    __file__ = testname

    # setup workspace and start the case
    createWdir()
    import time, platform
    print '*' * 80
    print "starting case", testname
    print "time:", time.strftime("%c")
    print "hostname:", platform.node()
    print '*' * 80
    print '* pyNav'
    print '* Adrien Crovato'
    print '* 2019'
    print '* Distributed under Apache license 2.0'
    print '*' * 80
    execfile(testname)

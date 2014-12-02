#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A script showing how to use optparse.'''

__author__ = 'Russel Winder'
__date__ = '2013-03-03'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2013  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from optparse import OptionParser


def createParser():
    parser = OptionParser(usage='Usage: %prog [options]')
    parser.add_option('-v', '--verbose', action='count', dest='verboseCount', help='say more than usual')
    parser.add_option('-q', '--quiet', action='count', dest='quietCount', help='be more quiet than usual')
    return parser


def processLevel():
    (options, args) = createParser().parse_args()
    outputLevel = 0
    if options.verboseCount:
        outputLevel += options.verboseCount
    if options.quietCount:
        outputLevel -= options.quietCount
    return outputLevel


if __name__ == '__main__':
    print(processLevel())

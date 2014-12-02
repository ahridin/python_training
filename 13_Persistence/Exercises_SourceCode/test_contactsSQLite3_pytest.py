#! /usr/bin/env py.test-3

'''
Test contacts database realized using SQLite3
'''

__author__ = 'Russel Winder'
__date__ = '2014-07-23'
__version__ = '1.3'
__copyright__ = 'Copyright © 2010–2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

from unittest import main

import contacts_test_class
from contacts_test_class import TestContacts

from contactsSQLite3 import Connection

contacts_test_class.url = ':memory:'
contacts_test_class.ConnectionClass = Connection

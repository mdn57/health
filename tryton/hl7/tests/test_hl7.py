#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2015 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2015 GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2015 CRS4
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import sys
import os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__, '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class HL7TestCase(unittest.TestCase):
    """
    Test HL7 module.
    """

    def setUp(self):
        trytond.tests.test_tryton.install_module('hl7')

    def test0005views(self):
        """
        Test views.
        """
        test_view('hl7')

    def test0006depends(self):
        """
        Test depends.
        """
        test_depends()


def suite():
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(HL7TestCase))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

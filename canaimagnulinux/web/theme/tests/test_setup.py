# -*- coding: utf-8 -*-

"""
This is an integration "unit" test.
"""

from Products.CMFCore.utils import getToolByName

# from canaimagnulinux.web.theme.config import DEPENDENCIES
from canaimagnulinux.web.theme.config import PROJECTNAME
# from canaimagnulinux.web.theme.interfaces import ICanaimaGNULinuxLayer
from canaimagnulinux.web.theme.testing import INTEGRATION_TESTING

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.browserlayer.utils import registered_layers

import unittest


class InstallTestCase(unittest.TestCase):
    """
    The class that tests the installation of a particular product.
    """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')

    def test_installed(self):
        """
        This method test the default GenericSetup profile of this package.
        """
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

#    def test_dependencies_installed(self):
#        """
#        This method test that dependencies products are installed of this package.
#        """
#        for p in DEPENDENCIES:
#            self.assertTrue(self.qi.isProductInstalled(p),
#                            '{0} not installed'.format(p))

    def test_addon_layer(self):
        """
        This method test if the ICanaimaGNULinuxLayer is available.
        """
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('ICanaimaGNULinuxLayer' in layers,
                        'add-on layer was not installed')


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

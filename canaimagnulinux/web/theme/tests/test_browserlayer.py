# -*- coding: utf-8 -*-

from canaimagnulinux.web.theme.config import PROJECTNAME
from canaimagnulinux.web.theme.interfaces import ICanaimaGNULinuxLayer
from canaimagnulinux.web.theme.testing import INTEGRATION_TESTING

from plone.browserlayer.utils import registered_layers
from zope.site.hooks import setSite

import unittest


class TestBrowserLayer(unittest.TestCase):
    """Ensure browser layer is installed and uninstalled properly."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        portal = self.layer['portal']
        setSite(portal)
        self.portal = portal
        self.qi = getattr(self.portal, 'portal_quickinstaller')

    def test_installed(self):
        """ This method test if the ICanaimaGNULinuxLayer is available. """
        self.assertTrue(ICanaimaGNULinuxLayer in registered_layers(), 'add-on layer was not installed')

    def test_uninstalled(self):
        """ This method test if the ICanaimaGNULinuxLayer is uninstalled. """
        self.qi.uninstallProducts(products=[PROJECTNAME])
        self.assertTrue(ICanaimaGNULinuxLayer not in registered_layers())

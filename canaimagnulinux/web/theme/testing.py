# -*- coding: utf-8 -*-

"""
This layer is the Test class base.

Check out all tests on this package:

./bin/test -s canaimagnulinux.web.theme --list-tests
"""

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile

from plone.testing.z2 import ZSERVER_FIXTURE
from plone.testing.z2 import installProduct
from plone.testing.z2 import uninstallProduct


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):

        # Load ZCML

        import plone.api
        self.loadZCML(package=plone.api)

        import canaimagnulinux.web.theme
        self.loadZCML(package=canaimagnulinux.web.theme)

        # Install products that use an old-style initialize() function
        installProduct(app, 'canaimagnulinux.web.theme')

    def tearDownZope(self, app):
        # Uninstall products installed above
        uninstallProduct(app, 'canaimagnulinux.web.theme')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'canaimagnulinux.web.theme:default')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='canaimagnulinux.web.theme:Integration'
)

"""
We use this for functional integration tests. Again, we can put basic
common utility or setup code in here.
"""
ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZSERVER_FIXTURE),
    name='canaimagnulinux.web.theme:Acceptance'
)

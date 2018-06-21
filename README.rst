=========================
canaimagnulinux.web.theme
=========================

A theme for `Canaima GNU/Linux community`_ website.


Introduction
============

*Canaima Kerepakupai* Theme is an installable Plone Theme developed by 
`Canaima GNU/Linux community`_ using the **theming**- and **packaging**- 
features available in `plone.app.theming`_.

This product contains a Diazo_ theme in Plone 4.3 for the `Canaima GNU/Linux website`_. 
Let you integrate Plone CMS elements visual, social networks and other web applications 
in a unique GUI.


About QA
--------

.. image:: https://d2weczhvl823v0.cloudfront.net/CanaimaGNULinux/canaimagnulinux.web.theme/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

.. image:: https://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.theme.svg?branch=master
   :alt: Travis-CI badge
   :target: https://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.theme

.. image:: https://coveralls.io/repos/CanaimaGNULinux/canaimagnulinux.web.theme/badge.png?branch=master
   :alt: Coveralls badge
   :target: https://coveralls.io/r/CanaimaGNULinux/canaimagnulinux.web.theme?branch=master


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/CanaimaGNULinux/canaimagnulinux.web.theme/raw/master/canaimagnulinux/web/theme/diazo_resources/preview.png


Features
========

- It's an installable Plone_ Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo_ package (Zip file).
- It's have support for clean uninstallation.


Installation
============

You can read the ``INSTALL.txt`` file inside the ``docs`` folder for this package.

Zip file
--------

If you are an end user, you might enjoy installation via zip file import.

1. Download a `zip file <https://github.com/CanaimaGNULinux/canaimagnulinux.web.theme/raw/master/canaimagnulinux.web.theme.zip>`_.
2. Import the theme from the Diazo_ theme control panel.


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``canaimagnulinux.web.theme`` package add it to your ``buildout`` section's 
*eggs*- parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        canaimagnulinux.web.theme


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'canaimagnulinux.web.theme',
    ],


Enabling the theme
^^^^^^^^^^^^^^^^^^

Select and enable the theme from the Diazo_ control panel. That's it!


Contribute
==========

- Issue Tracker: https://github.com/CanaimaGNULinux/canaimagnulinux.web.theme/issues
- Source Code: https://github.com/CanaimaGNULinux/canaimagnulinux.web.theme


License
=======

The project is licensed under the GPLv2.


Credits
=======


Authors
-------

- Maximiliano Vilchez aka maxudes.

- Leonardo J .Caballero G. aka macagua.


Amazing contributions
---------------------

- Axel Díaz aka Axelio

- Dehivis Perez aka dehivix

- Rodrigo Bravo aka goidor

- Eliezer Romero aka eliezerfot123

- Miguel Sanabria aka masc1293

- Ericka Simancas aka erickaackseriam


You can find an updated list of package contributors on https://github.com/canaimagnulinux/canaimagnulinux.web.theme/contributors


.. _`Plone`: http://plone.org
.. _`Diazo`: https://pypi.org/project/diazo
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Canaima GNU/Linux community`: https://github.com/canaimagnulinux/
.. _`Canaima GNU/Linux website`: http://canaima.softwarelibre.gob.ve/

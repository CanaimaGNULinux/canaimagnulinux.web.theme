from setuptools import setup, find_packages
import os

# the package name
name='canaimagnulinux.web.theme'
version = '0.1'
# get packages from the package name: '1.2.3' -> ['1','1.2','1.2.3']
packages = [name.rsplit('.',x)[0] for x in reversed(range(len(name.split('.'))))]

setup(name=name,
      version=version,
      description="Canaima GNU/Linux Kerepakupai Theme, is an installable Diazo theme for Plone 4",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: Groupware",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='canaima gnu linux website kerepakupai theme',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/CanaimaGNULinux/canaimagnulinux.web.theme',
      license='GPLv2',
      # get packages from the package name: '1.2.3' -> ['1','1.2','1.2.3']
      packages = packages,
      # all except the last are treated as namespace_packages like ['1', '1.2'],
      namespace_packages = packages[:-1],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
#          'collective.cover==1.0a8.post1',
          'plone.api',
      ],
      extras_require={
          'test': [
              'plone.app.robotframework',
              'plone.app.testing [robot] >=4.2.2',
              'plone.browserlayer',
              'plone.testing',
              'robotsuite',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

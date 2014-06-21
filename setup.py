from setuptools import setup, find_packages
import os

# the package name
name='canaimagnulinux.web.theme'
version = '0.1'
# get packages from the package name: '1.2.3' -> ['1','1.2','1.2.3']
packages = [name.rsplit('.',x)[0] for x in reversed(range(len(name.split('.'))))]

setup(name=name,
      version=version,
      description="Canaima GNU/Linux Website Kerepakupai Theme",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
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
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

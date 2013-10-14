from setuptools import setup, find_packages
import os

version = '0.1'

setup(# the package name
      name='canaimagnulinux.web.theme',
      version=version,
      description="Canaima GNU/Linux Website Kerepakupai Theme",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='canaima gnu linux website kerepakupai theme',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/CanaimaGNULinux/canaimagnulinux.web.theme',
      license='gpl',
      # get packages from the package name: '1.2.3' -> ['1','1.2','1.2.3']
      packages = [name.rsplit('.',x)[0] for x in reversed(range(len(name.split('.'))))],
      # all except the last are treated as namespace_packages
      namespace_packages = packages[:-1],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

#from __future__ import unicode_literals
#from os.path import abspath, dirname, join
from setuptools import setup


#def read_relative_file(filename):
 #   """Returns contents of the given file, whose path is supposed relative
##    to this module."""
#    with open(join(dirname(abspath(__file__)), filename)) as f:
#        return f.read()


#if __name__ == '__main__':  # ``import setup`` doesn't trigger setup().
#    setup(
        
        
#    )

#!/usr/bin/env python

from distutils.core import setup

setup(
      name='django-x509',
      version='1.0',
      description='x509',
      author='Pulina',
      author_email='no@mail.com',
      url='https://github.com/pulina/django-x509/',
      packages=['setuptools', 'flask', 'django-uuidfield', 'pyOpenSSL'],
     )

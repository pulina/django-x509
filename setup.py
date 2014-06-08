from __future__ import unicode_literals
from os.path import abspath, dirname, join
from setuptools import setup


def read_relative_file(filename):
    """Returns contents of the given file, whose path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()


if __name__ == '__main__':  # ``import setup`` doesn't trigger setup().
    setup(
        name='django-x509',
        version=read_relative_file('VERSION').strip(),
        description="Let you be behind a nginx configuration an get x509 auth credentials",
        packages='x509',
        include_package_data=True,
        zip_safe=False,
        install_requires=('setuptools', 'flask', 'django-uuidfield', 'pyOpenSSL')
    )

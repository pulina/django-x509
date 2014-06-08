from setuptools import setup, find_packages
import os

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
extensions_dir = 'x509'

if __name__ == '__main__':  # ``import setup`` doesn't trigger setup().
    setup(
        name='django-x509',
        version='1.0',
        description="Let you be behind a nginx configuration an get "
                    "x509 auth credentials",
        long_description="",
        classifiers=['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3'],
        keywords='django wsgi x509 auth',
        author='Remy Hubscher',
        author_email='hubscher.remy@gmail.com',
        url='https://github.com/novapost/django-x509',
        license='MIT Licence',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=['setuptools>=1.1.6', 'flask', 'django-uuidfield',
                          'pyOpenSSL'],
        entry_points={
            'console_scripts': [
            'test_app = x509.test_app:main',
            ]
        }
    )
                    

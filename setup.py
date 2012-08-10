from setuptools import setup
 
setup(
    name = 'hammock',
    packages = ['hammock'],
    version = '0.0.1',
    description = 'rest like a boss',
    author='Kadir Pekel',
    author_email='kadirpekel@gmail.com',
    url='https://github.com/kadirpekel/hammock',
    install_requires=[
        'wrest>=0.1.0'
    ],
)
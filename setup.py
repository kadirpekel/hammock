from setuptools import setup
 
setup(
    name = 'hammock',
    packages = ['hammock'],
    version = '0.0.7',
    description = 'rest like a boss',
    author='Kadir Pekel',
    author_email='kadirpekel@gmail.com',
    url='https://github.com/kadirpekel/hammock',
    install_requires=[
        'requests>=0.13.6'
    ],
)

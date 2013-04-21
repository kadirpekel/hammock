from setuptools import setup

setup(
    name='hammock',
    py_modules=['hammock'],
    version='0.2.4',
    description='rest like a boss',
    author='Kadir Pekel',
    author_email='kadirpekel@gmail.com',
    url='https://github.com/kadirpekel/hammock',
    install_requires=[
        'requests>=1.1.0'
    ],
    tests_require=['httpretty==0.5.4'],
)

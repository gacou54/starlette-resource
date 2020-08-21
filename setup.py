from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='starlette-resource',
    version='0.1.0',
    packages=['tests', 'starlette_resource'],
    url='https://github.com/gacou54/starlette-resource',
    license='MIT',
    author='Gabriel Couture',
    author_email='gacou54@gmail.com',
    description='Starlette resource that helps you follow a layered architecture.',
    package=['starlette_resource'],
    install_requires=['starlette'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)

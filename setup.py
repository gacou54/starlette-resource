from setuptools import setup

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
    install_requires=['starlette']
)

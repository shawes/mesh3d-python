try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    description='Package to measure rugosity of 3D meshes',
    long_description=readme,
    author='Steve Hawes',
    url="https://github.com/shawes/mesh3d-python",
    author_email="maxhawes@gmail.com",
    install_requires=['pytest','numpy'],
    scripts=[],
    name='Mesh3D',
    version="0.1",
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

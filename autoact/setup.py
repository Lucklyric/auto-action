from setuptools import setup,find_packages
from autox import version

setup(
    name = 'autox',
    version = version,
    author = 'Xinyao(Alvin) Sun',
    author_email = 'xinyao1@ualberta.ca',
    packages = find_packages(),
    install_requires = [
        'numpy',
    ]
)

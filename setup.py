from setuptools import setup,find_packages
from autoact import __version__ as version

setup(
    name = 'auto-action',
    version = version,
    author = 'Xinyao(Alvin) Sun',
    author_email = 'xinyao1@ualberta.ca',
    packages = find_packages(),
    install_requires = [
        'pyyaml',
    ],
    entry_points = {
        'console_scripts': ['autoact=autoact.autoact:main']
    }
)

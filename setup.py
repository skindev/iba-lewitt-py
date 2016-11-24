try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# read the contents of the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

config = {
    'author': 'Andrew and Shamin',
    'author_email': 'skin.dev.null@gmail.com',
    'description': 'IBA Lewitt',    
    'name': 'iba_lewitt_py',    
    'packages': ['iba', 'data'],
    'version': '0.1',
    'download_url': 'Where to download it.',
    'install_requires': 'requirements',
    'scripts': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]    
}

setup(**config)

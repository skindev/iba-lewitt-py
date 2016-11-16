try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'author': 'Andrew and Shamin',
    'author_email': 'skin.dev.null@gmail.com',
    'description': 'IBA Lewitt',    
    'name': 'iba_lewitt_py',    
    'packages': ['iba'],    
    'version': '0.1',
    'download_url': 'Where to download it.',
    'install_requires': ['nose'],
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

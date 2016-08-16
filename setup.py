from distutils.core import *

setup(
    name="itemhut",
    version="0.1.0.dev1",
    description="open source ecommerce system in Python3",
    author="David",
    author_email="dbtoomey@gmail.com",
    license="MPLv2.0",
    install_requires=[
        "bottle>=0.12.9",
        "psycopg2>=2.6.2",
        "Beaker>=1.8.0",
        "bcrypt>=3.1.0",
        "py_bcrypt>=0.4",
        "google_api_python_client"
    ],

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Operating System :: Linux",
        "License :: OSI Approved :: Mozilla Public License Version 2.0"
    ])

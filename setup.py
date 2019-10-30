from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(  
    name="scrapyMysql",  
    version="0.1.2",  
    author="Lgchaos",  
    author_email="984684973@qq.com",  
    description="make scrapy store data into mysql easier",   
    license="MIT",  
    url="https://github.com/MRLGC/scrapyMysql",  
    packages=['scrapyMysql'],  
    install_requires=[  
        'attrs==18.1.0',
        'Automat==0.6.0',
        'constantly==15.1.0',
        'hyperlink==18.0.0',
        'idna==2.6',
        'incremental==17.5.0',
        'mysql-connector==2.1.6',
        'six==1.11.0',
        'Twisted==19.7.0',
        'zope.interface==4.5.0',
        ],
    keywords = 'scrapy',  
    classifiers=[  
        "Environment :: Web Environment",  
        "Intended Audience :: Developers",  
        "Operating System :: OS Independent",  
        "Topic :: Text Processing :: Indexing",  
        "Topic :: Utilities",  
        "Topic :: Internet",  
        "Topic :: Software Development :: Libraries :: Python Modules",  
        "Programming Language :: Python",  
        "Programming Language :: Python :: 3.6",    
    ],  
)  
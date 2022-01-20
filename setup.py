# -*- coding: utf-8 -*-

import setuptools
from os.path import join, dirname
from zymod import __version__

with open(join(dirname(__file__), 'requirements.txt'), 'r', encoding='utf-8') as f:
    pkgs = f.read()
    print('pkgs', pkgs)
    install_requires = pkgs.split("\n")

setuptools.setup(
    name='zymod',
    version=__version__,
    url='https://gitee.com/warp-drive-tech/libzymod-python',
    author='Chengdu Geek Camp',
    author_email='lq@cdgeekcamp.com',
    description='ZhiYan Python SDK',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=['zymod'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

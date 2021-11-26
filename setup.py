import os
import setuptools

setuptools.setup(
    name='python_sdk',
    version='1.0.2',
    url='https://github.com/Lixi20/python-sdk',
    author='Chengdu Geek Camp',
    author_email='lq@cdgeekcamp.com',
    description="zhiyan python sdk",
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    packages=['python_sdk'],
    license='MIT'
)

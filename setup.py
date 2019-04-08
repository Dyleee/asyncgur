from distutils.core import setup
setup(
    name='pygur',
    version='0.1',
    packages=['pygur',],
    license='MIT License',
    install_requires=['aiohttp', 'dacite',]
    long_description='''An Python Imgur Wrapper implementing Asynchronous Programming using Asyncio''',
)

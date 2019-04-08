from distutils.core import setup

setup(
    name='asyncgur',
    version='0.1',
    packages=['asyncgur',],
    license='MIT License',
    install_requires=['aiohttp', 'dacite',],
    long_description=open('README.md').read(),
    author='Dylee',
    author_email='dylee@mewbot.me',
)

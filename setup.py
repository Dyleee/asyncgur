from distutils.core import setup
with open('README.md') as f:
    long_desc = f.read()

setup(
    name='pygur',
    version='0.1',
    packages=['pygur',],
    license='MIT License',
    install_requires=['aiohttp', 'dacite',]
    long_description=long_desc,
    author='Dylee',
    author_email='dylee@mewbot.me',
)

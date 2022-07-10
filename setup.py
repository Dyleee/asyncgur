from distutils.core import setup

setup(
    name='asyncgur',
    version='0.1.1',
    packages=['asyncgur',],
    license='LGPLv3',
    install_requires=['aiohttp', 'dacite',],
    long_description=open('README.md').read(),
    keywords=["asyncio", "imgur", "async", "aiohttp", "pil", "pillow", "image", "upload",],
    author='Dylee',
    author_email='eelyd@protonmail.com',
    url="https://github.com/Dyleee/asyncgur",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

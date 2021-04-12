from setuptools import setup

setup(
    name ='homescrapper',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": }

)
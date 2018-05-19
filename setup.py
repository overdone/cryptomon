from setuptools import setup

setup(
    name='cryptomon',
    packages=['cryptomon'],
    include_package_data=True,
    install_requires=[
        'Flask>=1.0.2',
        'requests>=2.18.4',
        'APScheduler>=3.5.1'
    ],
)
from setuptools import find_packages, setup

setup(
    name='FitTrainer',
    author='sonnytron',
    url='https://github.com/sonnytron/FitTrainerBackEnd',
    packages=find_packages(),
    install_requires=[
        'dj_database_url',
        'Django >= 1.11, < 1.12',
        'djangorestframework',
        'envdir',
        'raven',
    ],
    entry_points={
        'console_scripts': [
            'fittrainer = FitTrainer.manage:main'
        ],
    }
)

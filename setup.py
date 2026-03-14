from setuptools import setup, find_packages

setup(
    name='fee-extraction-agent',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'pandas>=1.1.5',
        'numpy>=1.19.2',
    ],
    entry_points={
        'console_scripts': [
            'fee-extraction-agent=fee_extraction_agent.main:main',
        ],
    },
)
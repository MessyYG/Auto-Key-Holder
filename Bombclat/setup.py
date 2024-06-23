from setuptools import setup, find_packages

setup(
    name='bombclat',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pynput',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'bombclat = bombclat.main:main',
        ],
    },
    author='MessyYG',
    author_email='.',
    description='A script to toggle key press events in games.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/bombclat',
)
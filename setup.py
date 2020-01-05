from setuptools import setup


def readme_file_contents():
    with open('README.rst', 'r') as myfile:
        return myfile.read()

setup(
    name = 'NanoPot_test',
    version = '1.0.0',
    description = 'Simple TCP Honeypot;',
    long_description = readme_file_contents(),
    author = 'kimdavid333',
    author_email = 'kimdavid333@gmail.com',
    licence = 'MIT',
    packages=['nanopot'],
    scripts = [ 'bin/nanopot', 'bin/nanopot.bat'],
    zip_false=False,
    install_requires=['docopt']
)
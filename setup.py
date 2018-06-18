from setuptools import setup

setup(
    name='poseidonml',
    version='0.1.0',
    packages=['utils'],
    install_requires=['numpy==1.13.3', 'pika==0.11.0', 'redis==2.10.6', 'scikit-learn==0.18.2', 'scipy==1.0.0', 'tensorflow==1.3.0'],
    license='Apache License 2.0',
    author='cglewis',
    author_email='clewis@iqt.org',
    maintainer='Charlie Lewis',
    maintainer_email='clewis@iqt.org',
    description=('A utility package for extracting and analyzing features in network traffic.'),
    keywords='machine learning network analysis utilities',
    url='https://github.com/CyberReboot/PoseidonML',
)
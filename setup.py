from setuptools import find_packages,setup

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='vaibhav pandey',
    author_email='vaibhavmpandey10@gmail.com',
    install_requires=["pandas","scikit-learn","numpy"],
    packages=find_packages()
)
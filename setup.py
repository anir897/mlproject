from setuptools import find_packages,setup
from typing import List

def getrequirements(file_path:str)->list:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name="ml_project",
    version="0.0.1",
    author="anirvan das",
    author_email="anirvandas24@gmail.com",
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt'),
)

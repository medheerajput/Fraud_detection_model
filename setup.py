from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    # this function will return the list of requirements
    HYPHEN_E_DOT='-e .'
    requirements=[];
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
     
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="Fraud_Detection_model",
    version='0.0.1',
    author="Dheeraj",
    author_email="medheerajput@gmail.com",
    requires=get_requirements("requirements.txt")
)